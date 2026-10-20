def menu_print(items):
    for item in items:
        print(item)

# LEVEL 1 — MAIN MENU
while True:
    items = ["\nMAIN MENU", "1) Select Client", "2) Reports"]
    menu_print(items)  # Display Level 1 menu

    choice = input("Choice (Enter to exit): ")  # Wait for input

    if choice == "": break  # Exit Main Menu and end program
    elif choice == "1":     # Navigate to Level 2 — Select Client Menu
        while True:
            items = ["\nSELECT CLIENT MENU", "1) Bob", "2) Sue"]
            menu_print(items) # Display Level 2 menu

            choice = input("Choice (Enter to go back): ")  # Wait for input

            if choice == "": break # Return to Main Menu
            elif choice == "1":    # Navigate to Level 3 — Bob Menu
                while True:
                    items = ["\nBOB MENU", "1) Show Balance", "2) Show Transactions"]
                    menu_print(items)       # Display Level 3 menu

                    choice = input("Choice (Enter to go back): ")  # Wait for input

                    if choice == "": break  # Return to Select Client Menu
                    elif choice == "1":     # Perform action — remain in Bob Menu
                        print("Bob's balance: $1,000")
                    elif choice == "2":     # Perform action — remain in Bob Menu
                        print("Bob's transactions")

            elif choice == "2":    # Navigate to Level 3 — Sue Menu
                while True:
                    items = ["\nSUE MENU", "1) Show Balance", "2) Show Transactions"]
                    menu_print(items)       # Display Level 3 menu

                    choice = input("Choice (Enter to go back): ")  # Wait for input

                    if choice == "": break  # Return to Select Client Menu
                    elif choice == "1":     # Perform action — remain in Sue Menu
                        print("Sue's balance: $2,000")
                    elif choice == "2":     # Perform action — remain in Sue Menu
                        print("Sue's transactions")

    elif choice == "2":     # Navigate to Level 2 — Reports Menu
        while True:
            items = ["\nREPORTS MENU", "1) Client Reports", "2) Group Reports"]
            menu_print(items)  # Display Level 2 menu

            choice = input("Choice (Enter to go back): ")  # Wait for input

            if choice == "": break  # Return to Main Menu
            elif choice == "1":     # Navigate to Level 3 — Client Reports Menu
                while True:
                    items = ["\nCLIENT REPORTS MENU", "1) Show Clients", "2) Show Holdings"]
                    menu_print(items)      # Display Level 3 menu

                    choice = input("Choice (Enter to go back): ")  # Wait for input

                    if choice == "": break  # Return to Reports Menu
                    elif choice == "1":     # Perform action — remain in Client Reports Menu
                        print("Showing clients")
                    elif choice == "2":     # Perform action — remain in Client Reports Menu
                        print("Showing holdings")

            elif choice == "2":     # Navigate to Level 3 — Group Reports Menu
                while True:
                    items = ["\nGROUP REPORTS MENU", "1) Show Summary", "2) Show Performance"]
                    menu_print(items)  # Display Level 3 menu

                    choice = input("Choice (Enter to go back): ")  # Wait for input

                    if choice == "": break  # Return to Reports Menu
                    elif choice == "1":     # Perform action — remain in Group Reports Menu
                        print("Showing group summary")
                    elif choice == "2":     # Perform action — remain in Group Reports Menu
                        print("Showing group performance")
print("Logged off.")


"""
                                        LEVEL 1 — MAIN MENU
                                                 |
                          +----------------------+----------------------+
                          |                                             |
                     Select Client                                   Reports
                          |                                             |
                       LEVEL 2                                       LEVEL 2 
                  SELECT CLIENT MENU                               REPORTS MENU
                          |                                             |
                +---------+---------+                         +---------+---------+
                |                   |                         |                   |
               Bob                 Sue                  Client Reports       Group Reports
                |                   |                         |                   |
             LEVEL 3             LEVEL 3                   LEVEL 3          LEVEL 3 GROUP
             BOB MENU            SUE MENU              CLIENTS REP MENU     GROUP REP MENU
                |                   |                         |                   |
          +-----+-----+       +-----+-----+             +-----+-----+       +-----+-----+
          |           |       |           |             |           |       |           |
         Show        Show    Show        Show          Show        Show    Show        Show
        Balance     Trans.  Balance     Trans.        Clients    Holdings Summary   Performance
          |           |       |           |             |           |       |           |
        Action      Action  Action      Action        Action      Action  Action      Action


NAVIGATION RULES
----------------

1. Each menu has its own while True loop.

2. Selecting a submenu enters a nested while loop.

3. Selecting an action performs an operation and stays in the same menu.

4. Pressing Enter executes break, exiting the current while loop.

5. Exiting a submenu returns to the enclosing menu's loop.

6. Pressing Enter at the Main Menu ends the program.


STATE
-----

The active menu is determined by which while loop is executing.

The program does not store the current menu in a variable.

Navigation state is implicit in the program's control flow.

The deeper the menu hierarchy, the more nested the program becomes.
"""





