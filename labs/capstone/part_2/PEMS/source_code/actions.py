from pprint import pprint as pp
from pause import pause
from clear_screen import clear
from save_pems import save_pems
from del_pems import del_pems
from copy import deepcopy
import sys
import math

def select_client(state):
    clear()
    # clients is a list. client_idx is the index number in that list of our selected client.
    # PEMS uses a dictionary called state to pass in information to our action functions
    state['client_idx'] = None

    # clients are the list of client dicts for logged in manager
    clients = state['clients']
    
    if len(clients) == 0:
        print('You have no clients. Create a client')
        pause(2)
        return False   # returning False will keep you on the same menu    
    else:
        # will print out each of our clients
        for idx, client in enumerate(clients, 1):
            print(f"{idx}) {client['name']}")

        print()
        txt = 'choice: '
        while True:
            entry = input(txt).strip()
            if entry == '':
                return False          # cancel: stay on Client Management
            try:
                choice = int(entry)
                if 1 <= choice <= len(clients):
                    break
            except ValueError:
                pass
            txt = 'Enter a valid choice (Enter to cancel): '

        # we update state['client_idx'] with the client we want to work with
        state['client_idx'] = choice - 1        
        
        rebuild_holdings(state)

        
        # the function returns none and goes back to PEMS.py inside the while loop
        # and navigates to client_workspace
        
        
    

def create_client(state):
    clear()
    state['client_idx'] = None
    
    name = input("Enter Client Name: ").strip()
    email = input("Enter Client Email: ").strip()
    phone = input('Enter Client Phone Number: ').strip()    

    if '' in(name, email, phone):
        print('Client not created') 
        pause(2)
        return False        
    
    clients = state['clients'] # just a reference for easy access

    #TODO:  finish creating a client    
    client = {'name':name,
              'email': email,
              'phone': phone,
              'transactions': []}  

    
    # we need to be careful here
    # we need to append client to clients so we can add a transaction
    # to this client
    clients.append(client)
    state['client_idx'] = len(clients) - 1  

    transaction_created = contribution(state) 

    if transaction_created:                
        print('Client Created check json')        
    else:
        # if the transaction fails we need to remove the client we just appended
        del clients[state['client_idx']]
        print('Transaction failed, Client Not Created')

    pause(2)
    return False    

def contribution(state):    
    client = state['clients'][state['client_idx']]
    transactions = client['transactions']
    next_trns_id = len(transactions) + 1

    txt = 'Enter cash contribution: '
    
    while True:
        cash = input(txt).strip()
        if cash == '' : 
            print('Transaction not created')
            pause(2)
            return False
        try:
            cash = float(cash)
            if cash <= 0 : raise ValueError
            break
        except ValueError:
            txt = 'Enter a value greater than 0: '    

    transaction = {'trans_id': next_trns_id,
                    'trd_day': state['trd_day'],
                    'trans_type': 'CONTRIBUTION',
                    'ticker': '$$$$',
                    'shares': round(cash, 2),
                    'cps'   : 1.00,
                    'tot_cst': round(cash * 1.00, 2),
                    'div_amnt': 0,
                    'shares_before': 1,
                    'shares_after': 1
        } 

    transactions.append(transaction)
    print('Transaction created check json')
    # after every transactions we need to save pems.json
    save_pems(state)
    update_holdings(state)    
    pause(5)
    return True

    

def withdrawal(state):
    print("now what w")
    

def buy(state):
    print("now what b")
    

def sell(state):
    print("now what s")

def adv_trd_day(state):
    pass   


def update_holdings(state):
    
    positions = state['holdings']
    client_idx = state['client_idx']
    if state['advance']:
        positions[state['trd_day']] = deepcopy(positions.get(state['trd_day'] - 1, {}))
        state['advance'] = False
        return

    client = state['clients'][client_idx]
    transactions = client['transactions']
    transaction = transactions[-1]
    trd_day = state['trd_day']
    ticker = transaction['ticker']

    positions[trd_day][ticker] = positions[trd_day].get(ticker,{'shares':0,'total_cost':0})

    if transaction['trans_type'] in ['CONTRIBUTION', 'BUY']:
        positions[trd_day][ticker]['shares'] +=  transaction['shares']
        positions[trd_day][ticker]['total_cost'] += transaction['shares'] * transaction['cps']

    elif transaction['trans_type'] in ['WITHDRAWAL', 'SELL']:
        avg_price = positions[trd_day][ticker]['total_cost'] / positions[trd_day][ticker]['shares']
        positions[trd_day][ticker]['shares'] -=  transaction['shares']
        positions[trd_day][ticker]['total_cost'] -= transaction['shares'] * avg_price

    if round(positions[trd_day][ticker]['shares'], 2) == 0:
       if ticker == '$$$$':
           positions[trd_day][ticker]['total_cost'] = 0   # clear float residue
           positions[trd_day][ticker]['shares'] = 0
       else:
           del positions[trd_day][ticker]

    pp(positions)
    pp(state['holdings'])

def rebuild_holdings(state):
    client = state['clients'][state['client_idx']]
    transactions = client['transactions']

    state['holdings'] = {0: {}}
    state['advance'] = False

    for day in range(1, state['trd_day'] + 1):
        state['holdings'][day] = deepcopy(state['holdings'][day - 1])

        for transaction in transactions:
            if transaction['trd_day'] != day:
                continue

            ticker = transaction['ticker']

            state['holdings'][day][ticker] = state['holdings'][day].get(ticker, {'shares': 0, 'total_cost': 0})

            position = state['holdings'][day][ticker]

            if transaction['trans_type'] in ['CONTRIBUTION', 'BUY']:
                position['shares'] += transaction['shares']
                position['total_cost'] += transaction['shares'] * transaction['cps']

            elif transaction['trans_type'] in ['WITHDRAWAL', 'SELL']:
                avg_price = position['total_cost'] / position['shares']
                position['shares'] -= transaction['shares']
                position['total_cost'] -= transaction['shares'] * avg_price

            if round(position['shares'], 2) == 0:
                if ticker == '$$$$':
                    position['shares'] = 0
                    position['total_cost'] = 0
                else:
                    del state['holdings'][day][ticker]




    


# TODO update as needed
actions = {
    "select_client": select_client,    
    "create_client": create_client,
    "contribution": contribution,
    "withdrawal": withdrawal,
    "buy": buy,
    "sell": sell
}