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

    for day in range(len(tickers)):      

        daily_record = {'date': eod_prices[tickers[0]][day]['Date'][:10]}       

        for ticker in tickers:           

            ticker_record = {
                'price': eod_prices[ticker][day]['Close'],
                'div': 0,
                'split_in': 1,
                'split_out': 1
            }            

            for action in corporate_actions[ticker]:                

                action_date = action['Date'][:10]                

                if action_date == daily_record['date']:                   

                    ticker_record['div'] = action.get('Dividends', 0)
                    
                    split_factor = action.get('Stock Splits', 0)
                   
                    if split_factor:
                        ticker_record['split_out'], ticker_record['split_in'] = (
                            Decimal(str(split_factor)).as_integer_ratio()
                        )                   

                    break                

                if action_date > daily_record['date']:
                    break

            daily_record[ticker] = ticker_record
        
        market_data[day] = daily_record

    if False:
        for day in range(3):
            print(f"Day {day}:")
            pp(market_data[day], sort_dicts=False)

        
        
    return market_data, menus, pems, security_info


if __name__ == "__main__":
    load_data()



    