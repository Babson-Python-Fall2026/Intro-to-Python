from pprint import pprint as pp
from pause import pause
from clear_screen import clear
from save_pems import save_pems
def select_client(state):
    clear()
    state['client_idx'] = None
    clients = state['pems'][state['pm']]['clients']

    if not clients:
        print(f"{state['pm']} has no clients. Create Client.")
        pause(2)
        return False

    for i, client in enumerate(clients, 1):
        print(f"{i}) {client['name']}")

    txt = "Select Client (Enter to cancel): "
    while True:
        choice = input(txt)

        if choice == "":
            return False

        try:
            choice = int(choice)
            if 1 <= choice <= len(clients):
                state['client_idx'] = choice - 1
                return True
            else:
                raise ValueError
        except ValueError:
            txt = f"Select Client 1 - {len(clients)} (Enter to cancel): "

        print("Invalid client selection.")

        

def create_client(state):
    clear()
    
    name = input("Enter Client Name: ")
    email = input("Enter Client Email: ")
    phone = input('Enter Client Phone Number: ')

    clients = state['pems'][state['pm']]['clients']
    client =  {'name': name, 'email': email, 'phone': phone, 'transactions': []}
    
    state['client_idx'] = len(clients)

    clients.append(client)
    contribution(state)
    '''
    txt = 'Enter starting cash: '
    while True:
        try:
            cash = float(input(txt))
            if cash < 0:
                raise ValueError
            else:
                break
        except ValueError:
            txt = 'Enter a positive cash value: '
    cash = round(cash,2)

    trans_id = len(client['transactions']) + 1
    transaction = {'trans_id': trans_id,
                   'trd_day': state['trd_day'],
                   'ticker': '$$$$',
                   'trn_typ': 'CONTRIBUTION',
                   'shares': cash, 
                   'cps': 1.00,
                   'total_cost': cash }
    
    client['transactions'].append(transaction)
    '''
    

    
    
    



def buy(state):
    pass

def sell(state):
    pass

def contribution(state):
                      
    print('============================================')
    print('                CONTRIBUTION                ')
    print('============================================\n\n')

    txt = 'How much cash would you like to contribute? '
    while True:
        try:
            cash = float(input(txt))
            if  cash > 0:
                break
            else: raise ValueError
        except ValueError:
            txt = 'enter a positive amount (100_0000.00 or 100000.00): '

    client = state['clients'][state['client_idx']]
    transactions = client['transactions']

    trans_id = len(client['transactions']) + 1

    transaction = {'trans_id': trans_id,
                    'trd_day': state['trd_day'],
                    'ticker': '$$$$',
                    'trn_typ': 'CONTRIBUTION',
                    'shares': cash, 
                    'cps': 1.00,
                    'total_cost': cash }

    transactions.append(transaction)
    save_pems(state)
    print("contribution made")

def withdrawal(state):
    pass

def atd(state):
    pass

def report_holdings(state):
    pass

def report_transactions(state):
    pass

def report_performance(state):
    pass

def report_cash_summary(state):
    pass

actions = {
    "select_client": select_client,
    "create_client": create_client,    
    "buy": buy,
    "sell": sell,
    "contribution": contribution,
    "withdrawal": withdrawal,
    "atd": atd,
    "report_holdings": report_holdings,
    "report_transactions": report_transactions,
    "report_performance": report_performance,
    "report_cash_summary": report_cash_summary
}