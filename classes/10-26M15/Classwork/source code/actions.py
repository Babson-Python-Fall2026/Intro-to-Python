from pprint import pprint as pp
from pause import pause
from clear_screen import clear
from save_pems import save_pems
def select_client(state):
    clear()
    pm = state['pm']
    pems = state['pems']
    clients = pems[pm]['clients']
    
    if len(clients) == 0:
        print('You have no clients. Create a client')
        pause(2)
        return False
    else:
        for idx, client in enumerate(clients, 1):
            print(f"{idx}) {client['name']}")

        state['client_idx'] = 0
        return True
        
    

def create_client(state):
    clear()
    
    name = input("Enter Client Name: ")
    email = input("Enter Client Email: ")
    phone = input('Enter Client Phone Number: ')
    cash = input('Enter starting cash: ')

    if '' in(name,email,phone,cash): return False
    
    pm = state['pm']
    pems = state['pems']
    clients = pems[pm]['clients']

    

    client = {'name': name,
              'email': email,
              'phone': phone,
              'transactions': []}

    transactions = client['transactions']

    transaction = {'trans_id': len(transactions) + 1,
                   'trd_day': state['trd_day']}

    transactions.append(transaction)
    clients.append(client)

    save_pems(state)
    return False
    
    




actions = {
    "select_client": select_client,
    "create_client": create_client    
    
}