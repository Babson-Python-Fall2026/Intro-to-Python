from login import login
from clear_screen import clear
from pause import pause
from load_data import load_data
from pprint import pprint as pp

from menu_print import menu_print

clear()

def pems():
    while True:
        clear()
        current_pm = login()
        if current_pm is None: 
            clear()
            print("STATUS: No One Logged In")
            print("STATUS: LOG OFF")
            break

        print(f"{current_pm} is now logged in")
        pause(1)
        clear()

        market_data, MENUS, pems, security_info = load_data()

        stack = ["client_management"]
        state = {
                "pm": current_pm,
                'pems': pems,
                "clients": pems[current_pm]["clients"],
                "client_idx": None,
                "trd_day": 1,
                "market_data": market_data,
                "security_info": security_info
            }
        
        while stack:

            if stack[-1] == "client_management":
                state["client_idx"] = None
                client_name = None
            
            if state['client_idx'] is not None:
                client_name = pems[current_pm]['clients'][state['client_idx']]['name']
            
            cur_menu = MENUS[stack[-1]]
            menu_print(cur_menu, client_name)

            if len(stack) == 1:
                prompt = "Choice (Enter to exit): " 
            else:
                prompt = "Choice (Enter to go back): "

            choice = input(prompt).strip()

            if choice == "":
                stack.pop()
                continue
            if not choice.isdigit() or not (1 <= int(choice) <= len(cur_menu["options"])):
                print("Invalid choice.")
                continue

            option = cur_menu["options"][int(choice) - 1]

            if option["action"] is not None:
                if option["action"](state) is False:
                    continue         
            

            if option["next_menu"] is not None:
                stack.append(option["next_menu"])

        print("Logged off.")
        pause(2)


if __name__ == "__main__":
    pems()
