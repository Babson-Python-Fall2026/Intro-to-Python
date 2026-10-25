from pprint import pprint as pp
from pause import pause
from clear_screen import clear
from save_pems import save_pems
def select_client(state):
    clear()
    pp(state['pems'],width=120,sort_dicts=False)
    pause(2)
    return False
    

def create_client(state):
    clear()
    
    name = input("Enter Client Name: ")
    email = input("Enter Client Email: ")
    phone = input('Enter Client Phone Number: ')

    pp(state['pems'],width=120,sort_dicts=False)

    save_pems(state)
    return False
    
    




actions = {
    "select_client": select_client,
    "create_client": create_client    
    
}