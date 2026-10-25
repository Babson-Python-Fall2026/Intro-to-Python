import json
import hashlib
import hmac
import getpass

from pathlib import Path

def login():
   
    ITERATIONS = 600_000  

    DATA = (Path(__file__).parent.parent / "data").resolve()
    with open(DATA / "pm_users.json", "r", encoding="utf-8") as file:
        pm_users = json.load(file)
   
    while True:
        
        mgr = input("Enter pm initials: ").strip().upper()
        if mgr == '':return None

        pm = pm_users.get(mgr)
        if pm is None:
            print('Manager not found')
            continue

        password = getpass.getpass("Enter Password: ")
        
        salt = bytes.fromhex(pm["salt"])
        test_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), salt, ITERATIONS
        )
        if hmac.compare_digest(test_hash.hex(), pm["password_hash"]):
            return mgr
        else:
            print("password does not match, try again")
            

if __name__ == "__main__":
    login()   
