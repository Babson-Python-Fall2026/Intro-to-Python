from pprint import pprint as pp
from pause import pause
from clear_screen import clear
from save_pems import save_pems
def select_client(state):
    clear()
    
    clients = state['clients']
    
    if len(clients) == 0:
        print('You have no clients. Create a client')
        pause(2)
        return False   # returning False will keep you on the same menu    
    else:
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

        state['client_idx'] = choice - 1
        return True
        
    

def create_client(state):
    clear()
    client_created = True
    name = input("Enter Client Name: ").strip()
    email = input("Enter Client Email: ").strip()
    phone = input('Enter Client Phone Number: ').strip()
    cash = input('Enter starting cash: ').strip()

    if '' in(name,email,phone,cash): 
        client_created = False 

    try:
        cash = int(cash)
    except ValueError:
        client_created = False
        cash = 0

    if cash <= 0 : 
        client_created = False 

    if not client_created:
        print('Client not created')
        pause(2)
        return False

    
    clients = state['clients']

    #TODO:  finish creating a client
    CLIENT_KEYS = ["name", "email", "phone", "transactions"]
    client = {'name':name}
    
              

    transactions = client.get('transactions',[])

    
    #TODO: finish creating a transaction
    ''' 
    field	        value
    trans_id        len(transactions) + 1
    trd_day         state['trd_day']
    type	        "CONTRIBUTION"
    ticker	        "$$$$"
    shares	        the cash amount
    cost_per_share	1.0
    total       	the cash amount
    div_amnt, shares_before, shares_after	None    
    '''
    TRANSACTION_KEYS = ["trans_id", "trd_day", "type", "ticker", "shares",
                        "cost_per_share", "total", "div_amnt",
                        "shares_before", "shares_after"]
    transaction = {}

    transactions.append(transaction)
    clients.append(client)

    save_pems(state)
    print('Client Created')
    pause(2)
    
    
    




actions = {
    "select_client": select_client,
    "create_client": create_client    
    
}