import json
import sys

from pprint import pprint as pp
from decimal import Decimal

from clear_screen import clear
from actions import actions

from pathlib import Path

def load_data():

    DATA = (Path(__file__).parent.parent / "data").resolve()
    
    with open(DATA / "nyse_top100.json", "r", encoding="utf-8") as file:
        tickers = json.load(file)['tickers']

    with open(DATA / "corp_acts_yf.json", "r", encoding="utf-8") as file:
        corporate_actions = json.load(file)['data']

    with open(DATA / "raw_eod_yf.json", "r", encoding="utf-8") as file:
        eod_prices = json.load(file)['data']

    with open(DATA / "businessquant.json", "r", encoding="utf-8") as file:
        security_info = json.load(file)['data']

    with open(DATA / "menus.json", "r", encoding="utf-8") as file:
            menus = json.load(file)

    for menu in menus.values():
        for option in menu["options"]:
            action_name = option.get("action")

            if action_name is not None:
                option["action"] = actions[action_name]

    try:
        with open(DATA / "pm_users.json", "r", encoding="utf-8") as file:
            pm_users = json.load(file)
    except FileNotFoundError:
        print('FATAL ERROR: pm_users.json not found')
        sys.exit(1)

    try:
        with open(DATA / "pems.json", "r", encoding="utf-8") as file:
            pems = json.load(file)          
    except FileNotFoundError:
        print('FATAL ERROR: pms.json not found')
        sys.exit(1)

    if pm_users.keys() != pems.keys():
        print("FATAL ERROR: PM JSON files are not in sync.")
        sys.exit(1)    


    
    market_data = {}    

    

        
        
    return market_data, menus, pems, security_info


if __name__ == "__main__":
    load_data()



    