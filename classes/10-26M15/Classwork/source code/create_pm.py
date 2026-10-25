"""Create portfolio manager logins. Run: python create_pm.py"""

import getpass
import hashlib
import hmac
import json
import os
import sys

from pathlib import Path

ITERATIONS = 600_000

def verify_pm(initials, password, pm_users):
    """Return True if the PM initials and password are correct."""
    pm = pm_users.get(initials.strip().upper())
    if pm is None:
        return False

    salt = bytes.fromhex(pm["salt"])
    test_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, ITERATIONS
    )
    return hmac.compare_digest(test_hash.hex(), pm["password_hash"])

def main():
    try:

        DATA = (Path(__file__).parent.parent / "data").resolve()
        with open(DATA / "pm_users.json", "r", encoding="utf-8") as file:
            pm_users = json.load(file)
        
    except FileNotFoundError:
        pm_users = {}

    try:
        DATA = (Path(__file__).parent.parent / "data").resolve()

        with open(DATA / "pems.json", "r", encoding="utf-8") as file:
            pems = json.load(file)
        
    except FileNotFoundError:
        pems = {}

    if pm_users.keys() != pems.keys():
        print("FATAL ERROR: PM JSON files are not in sync.")
        sys.exit(1)

    while True:
        initials = input("PM initials (Enter to quit): ").strip().upper()
        if initials == "":
            break
        if not initials.isalpha() or not 2 <= len(initials) <= 6:
            print("Enter 2 to 6 letters.")
            continue
        if initials in pm_users:
            print("That PM already exists.")
            continue
      

        password = getpass.getpass("Password (6+ characters): ")
        if len(password) < 6 :
            print("Passwords must at least 6 characters.")
            continue

        confirmation = getpass.getpass("Password again: ")
        if password != confirmation:
            print("Passwords must match and have at least 6 characters.")
            continue

        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), salt, ITERATIONS
        )
        pm_users[initials] = {
            "salt": salt.hex(),
            "password_hash": password_hash.hex()
        }

        pems[initials] = {'clients':[] }

        DATA = (Path(__file__).parent.parent / "data").resolve()

        with open(DATA / "pm_users.json", "w", encoding="utf-8") as file:
            json.dump(pm_users, file, indent=2)            
        
        with open(DATA / "pems.json", "w", encoding="utf-8") as file:
            json.dump(pems, file, indent=2)     
        

        print(f"Created PM {initials}.")
        



if __name__ == "__main__":
    main()
