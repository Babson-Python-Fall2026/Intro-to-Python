from login import login
from clear_screen import clear
from pause import pause
from load_data import load_data
from pprint import pprint as pp
from actions import update_holdings
import json
from pathlib import Path

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

        # loading current trade day
        DATA = (Path(__file__).parent.parent / "data").resolve()    
        with open(DATA / "trd_day.json", "r", encoding="utf-8") as file:
            cur_trd_day = json.load(file)

        stack = ["client_management"]

        '''
        Instead of hard-coding the starting menu, let's establish a convention:
        the first key in the menus dictionary identifies the starting menu.
         '''

        menu_names = list(MENUS.keys())
        stack = [menu_names[0]]


        state = {
                "pm": current_pm,
                'pems': pems,
                "clients": pems[current_pm]["clients"],
                "client_idx": None,                
                "trd_day": cur_trd_day,
                "market_data": market_data,
                "security_info": security_info,
                "holdings": {0:{}},
                "advance": True
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
                txt = "Choice (Enter to exit): "
            else:
                txt = "Choice (Enter to go back): "

            while True:
                choice = input(txt).strip()
                if choice == '':
                    break
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(cur_menu['options']):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    txt = 'Enter a valid choice: '

            if choice == "":
                stack.pop()
                continue

            option = cur_menu["options"][choice - 1]

            if option.get("action") is not None:
                if option["action"](state) is False:
                    continue


            if option["next_menu"] is not None:
                stack.append(option["next_menu"])

        print("Logged off.")
        pause(2)


if __name__ == "__main__":
    pems()
