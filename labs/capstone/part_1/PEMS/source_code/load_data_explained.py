import json
import sys

from pprint import pprint as pp
from decimal import Decimal

from clear_screen import clear
from actions import actions

def load_data():

    with open("labs/capstone/part_1/PEMS/data/nyse_top100.json", "r", encoding="utf-8") as file:
        tickers = json.load(file)['tickers']

    with open("labs/capstone/part_1/PEMS/data/corp_acts_yf.json", "r", encoding="utf-8") as file:
        corporate_actions = json.load(file)['data']

    with open("labs/capstone/part_1/PEMS/data/raw_eod_yf.json", "r", encoding="utf-8") as file:
        eod_prices = json.load(file)['data']

    with open("labs/capstone/part_1/PEMS/data/businessquant.json", "r", encoding="utf-8") as file:
        security_info = json.load(file)['data']

    with open("labs/capstone/part_1/PEMS/data/menus.json", "r", encoding="utf-8") as file:
            menus = json.load(file)    

    # assign function names to option['action']
    for menu in menus.values():
        for option in menu["options"]:
            action_name = option["action"]

            if action_name is not None:
                option["action"] = actions[action_name]

    try:
        with open("labs/capstone/part_1/PEMS/data/pm_users.json", "r", encoding="utf-8") as file:
            pm_users = json.load(file)
    except FileNotFoundError:
        print('FATAL ERROR: pm_users.json not found')
        sys.exit(1)

    try:
        with open("labs/capstone/part_1/PEMS/data/pems.json", "r", encoding="utf-8") as file:
            pems = json.load(file)          
    except FileNotFoundError:
        print('FATAL ERROR: pms.json not found')
        sys.exit(1)

    if pm_users.keys() != pems.keys():
        print("FATAL ERROR: PM JSON files are not in sync.")
        sys.exit(1)       

    

    market_data = {}

    # eod_prices is a dictionary.
    # Each key is a ticker symbol (e.g., "TSM").
    # Each value is a list of 100 dictionaries, one per trading day.
    #
    # Example:
    #
    # eod_prices = {
    #     "TSM": [
    #         {
    #             "Date": "2025-08-15 00:00:00-04:00",
    #             "Open": 240.33,
    #             "High": 240.80,
    #             "Low": 237.26,
    #             "Close": 238.88,
    #             "Volume": 8155500
    #         },
    #         {...},  # Day 1
    #         {...},  # Day 2
    #         ...
    #     ],
    #     "AAPL": [...],
    #     ...
    # }

   
    # CONVERT THE ABOVE TO THE FOLLOWING:

    # Day 0:{'date': '2025-08-15',
    #        'TSM': {'price': 238.88, 'div': 0, 'split_in': 1, 'split_out': 1},
    #        'BRK.B': {'price': 477.2, 'div': 0, 'split_in': 1, 'split_out': 1},
    #        'LLY': {'price': 701.23, 'div': 1.5, 'split_in': 1, 'split_out': 1},

    # Day 1:{'date': '2025-08-18',
    #        'TSM': {'price': 241.41, 'div': 0, 'split_in': 1, 'split_out': 1},
    #        'BRK.B': {'price': 478.52, 'div': 0, 'split_in': 1, 'split_out': 1},
    #        'LLY': {'price': 698.05, 'div': 0, 'split_in': 1, 'split_out': 1},

    day = 0

    # STEP 1: Identify our first ticker.
    # For example, tickers[0] = "TSM"
    first_ticker = tickers[0]

    # STEP 2: Get its list of 100 daily records.
    ticker_records = eod_prices[first_ticker]

    # STEP 3: Select the record for the current trading day.
    # When day = 0, this is the first dictionary in the list.
    day_record = ticker_records[day]

    # STEP 4: Extract the date string.
    # "2025-08-15 00:00:00-04:00"
    date_string = day_record["Date"]

    # STEP 5: Keep only the first 10 characters.
    # "2025-08-15"
    date = date_string[:10]

    # STEP 6: Create the new daily record.
    daily_record = {"date": date}

    # all of that can be reduced to
    daily_record = {'date': eod_prices[tickers[0]][day]['Date'][:10]}

    ''' 
    We use the first ticker (tickers[0]) to obtain the date for each of our 100 daily_records.

    We can safely do this because our earlier examination and validation of the EOD data established 
    that all 100 tickers have exactly the same dates in exactly the same order.

    Therefore, the date at position day in the first ticker's records is also the date at that same 
    position for every other ticker.

    This is an important example of why we investigate and validate our data before writing the code 
    that processes it. Our earlier validation established an invariant that allows us to simplify the 
    construction of market_data.
    
    '''

    

    for day in range(100):     # for testing consider: for day in range(5)
        daily_record = {'date': eod_prices[tickers[0]][day]['Date'][:10]}
        for ticker in tickers: # for testing consider: for ticker in tickers[:5] 

            # get price from eod, set corp actions to default          
            ticker_record = {               
                             'price': eod_prices[ticker][day]['Close'],
                             'div': 0,
                             'split_in': 1,
                             'split_out': 1}            

            # check for corporate action
            for action in corporate_actions[ticker]:
                action_date = action['Date'][:10]
                if action_date == daily_record['date']:
                    
                    ticker_record['div'] = round(action.get('Dividends', 0), 2)
                    split_factor = action.get('Stock Splits', 1)

                    if split_factor:
                        ticker_record['split_out'], ticker_record['split_in'] = (
                            Decimal(str(split_factor)).as_integer_ratio() # look this up in ai!
                        )
                    break

                if action_date > daily_record['date']:
                    break

            # for every ticker               
            daily_record[ticker] = ticker_record  # create ticker key

        # for every day        
        market_data[day] = daily_record # create day key

    
    # pp(market_data, width = 120, sort_dicts = False)
    
    
    return market_data, menus, pems, security_info


if __name__ == "__main__":
    load_data()
    