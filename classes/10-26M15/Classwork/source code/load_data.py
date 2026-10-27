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
            action_name = option["action"]

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
        print('FATAL ERROR: pems.json not found')
        sys.exit(1)

    if pm_users.keys() != pems.keys():
        print("FATAL ERROR: PM JSON files are not in sync.")
        sys.exit(1)       

    print(pems.keys())
 
    market_data = {}
    

    ''' 
    market_data should look like:

    {0: {'date': '2025-08-15',
     'TSM': {'price': 238.88, 'div': 0, 'split_in': 1, 'split_out': 1},
     'BRK.B': {'price': 477.2, 'div': 0, 'split_in': 1, 'split_out': 1},
     'LLY': {'price': 701.23, 'div': 1.5, 'split_in': 1, 'split_out': 1},
     'JPM': {'price': 290.49, 'div': 0, 'split_in': 1, 'split_out': 1},
     'XOM': {'price': 106.49, 'div': 0.99, 'split_in': 1, 'split_out': 1}
     ... (for 100 tickers)},
 1: {'date': '2025-08-18',
     'TSM': {'price': 241.41, 'div': 0, 'split_in': 1, 'split_out': 1},
     'BRK.B': {'price': 478.52, 'div': 0, 'split_in': 1, 'split_out': 1},
     'LLY': {'price': 698.05, 'div': 0, 'split_in': 1, 'split_out': 1},
     'JPM': {'price': 291.53, 'div': 0, 'split_in': 1, 'split_out': 1},
     'XOM': {'price': 106.72, 'div': 0, 'split_in': 1, 'split_out': 1}},
 2: {'date': '2025-08-19',
     'TSM': {'price': 232.7, 'div': 0, 'split_in': 1, 'split_out': 1},
     'BRK.B': {'price': 485.31, 'div': 0, 'split_in': 1, 'split_out': 1},
     'LLY': {'price': 703.21, 'div': 0, 'split_in': 1, 'split_out': 1},
     'JPM': {'price': 290.66, 'div': 0, 'split_in': 1, 'split_out': 1},
     'XOM': {'price': 107.42, 'div': 0, 'split_in': 1, 'split_out': 1}},
 3: {'date': '2025-08-20',
     'TSM': {'price': 228.6, 'div': 0, 'split_in': 1, 'split_out': 1},
     'BRK.B': {'price': 488.68, 'div': 0, 'split_in': 1, 'split_out': 1},
     'LLY': {'price': 705.44, 'div': 0, 'split_in': 1, 'split_out': 1},
     'JPM': {'price': 292.24, 'div': 0, 'split_in': 1, 'split_out': 1},
     'XOM': {'price': 108.53, 'div': 0, 'split_in': 1, 'split_out': 1}},
... (for 100 days 0 -99)
    '''

    
    
    
    return market_data, menus, pems, security_info


if __name__ == "__main__":
    load_data()
    