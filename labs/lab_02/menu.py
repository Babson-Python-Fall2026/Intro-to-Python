import subprocess, sys
clients = ["bob", "sue", "alan", "debbie"]

def menu_input(max_choice):
    txt = "Choice (Enter to go back)"
    while True:        
        choice = input(f"{txt}: ").strip()
        
        if choice == "":
            return 0
        try:
            choice = int(choice)            
            if  1 <= choice <= max_choice :
                return int(choice)
            else:
                raise ValueError
        except ValueError:
           txt = f"Enter a number from 1 to {max_choice}"

def clear():
    subprocess.run("cls", shell=True)    
clear()
# LEVEL 1 - MAIN MENU
while True:
    clear()
    print("\nMAIN MENU")
    print("1) Create Client")
    print("2) Select Client")    

    choice = menu_input(2)

    if choice == 0 :
        break                       # Exit MAIN MENU

    if choice == 1:
        clear()
        name = input("Enter new client name: ").strip()
        if name:
            clients.append(name)
        # Terminal action is finished.  Main menu loop repeats.
    elif choice == 2:        
        # LEVEL 2 - SELECT CLIENT MENU        
        while True:
            clear()
            print("\nSELECT CLIENT")

            for i, client in enumerate(clients, start=1):
                print(f"{i}) {client}")
                if i%2 == 0: print()

            choice = menu_input(len(clients))

            if choice == 0:         # user pressed entered ""
                break               # Return to MAIN MENU

            selected_client = clients[choice - 1]

            # LEVEL 3 - CLIENT MENU            
            while True:
                clear()                
                print("1) Show Client")
                print("2) Rename Client")

                choice = menu_input(2)

                if choice == 0:
                    break           # Return to SELECT CLIENT
                if choice == 1:
                    clear()                    
                    print(f"Client: {selected_client}")
                    input("Press Enter to continue...")
                    # Terminal action completed. Client menu loop repeats.
                elif choice == 2:
                    clear()
                    name = input("New name: ").strip()

                    if name:
                        index = clients.index(selected_client)
                        clients[index] = name
                        selected_client = name
                    # Terminal action completed. Client menu loop repeats.

print("Logged off.")


''' 
LEVEL 1: Main Menu
    1) Create Client         → Action
    2) Select Client         → Go to Level 2
    3) Logoff                → Exit

    LEVEL 2: Select Client
        1) Bob               → Go to Level 3
        2) Sue               → Go to Level 3
        3) Alan              → Go to Level 3
        4) Debbie            → Go to Level 3
        Enter                → Return to Level 1

        LEVEL 3: Client Menu
            1) Show Client   → Action
            2) Rename Client → Action
            Enter            → Return to Level 2

'''
