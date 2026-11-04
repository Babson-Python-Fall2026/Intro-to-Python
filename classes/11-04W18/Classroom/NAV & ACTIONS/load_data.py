import json
import sys

from pprint import pprint as pp
from decimal import Decimal

from actions import actions

from pathlib import Path

def load_data(): 

    data =  Path(__file__).parent    
    
    with open(data / "menus.json", "r", encoding="utf-8") as file:
            menus = json.load(file)

    for menu in menus.values():
        for option in menu["options"]:
            action_name = option["action"]

            if action_name is not None:
                option["action"] = actions[action_name]       
        
    return  menus

if __name__ == "__main__":
    load_data()



    