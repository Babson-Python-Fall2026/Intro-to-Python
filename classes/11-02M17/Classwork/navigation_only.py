from pause import pause

nav_menus = {
    "client_management": {
        "title": "Client Management Menu",
        "options": [
            {"menu_item": "Select Client", "next_menu": "client_workspace"},
            {"menu_item": "Create Client", "next_menu": None},
        ],
    },
    "client_workspace": {
        "title": "Client Workspace",
        "options": [
            {"menu_item": "Transactions", "next_menu": "transactions"},
            {"menu_item": "Reports", "next_menu": "reports"},
        ],
    },
    "transactions": {
        "title": "Transactions",
        "options": [
            {"menu_item": "Not Implemented", "next_menu": None},            
        ],
    },
    "reports": {
        "title": "Reports",
        "options": [
            {"menu_item": "Not Implemented", "next_menu": None},            
        ],
    },
}



def display_nav_menu(current_menu):
    print("\n" + "=" * 36)
    print(current_menu["title"])
    print("=" * 36)
    for number, option in enumerate(current_menu["options"], 1):
        print(f"{number}) {option['menu_item']}")
    print("Press Enter to go back")


def run_navigation(menus):
    stack = ["client_management"]

    while stack:
        # 1. RETRIEVE: the name on top of the stack finds the menu (indirection).
        current_menu = menus[stack[-1]]
        display_nav_menu(current_menu)

        choice = input("Choice: ").strip()

        if choice == "":                  # go back
            stack.pop()
            continue

        if not choice.isdigit() or not 1 <= int(choice) <= len(current_menu["options"]):
            print("Invalid choice")
            continue

        # 2. SELECT: the numbered choice picks an option in this menu.
        option = current_menu["options"][int(choice) - 1]

        # 3. STORE: push the destination NAME; it is looked up next pass.
        if option["next_menu"] is not None:
            stack.append(option["next_menu"])
        else:
            print(f"\n{option['menu_item']}: no submenu — does nothing yet.")
            pause(2)
    print("Navigation finished.")


# OPTIONAL: uncomment to navigate interactively.
run_navigation(nav_menus)