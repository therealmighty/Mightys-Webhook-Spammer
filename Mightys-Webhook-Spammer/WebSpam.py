import os
import time

import colorama
import requests


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    inf = amount == "inf"
    while inf or counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name),
                                                "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"})
            if data.status_code == 204:
                print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}webhook deleted')
    print(f'{colorama.Fore.GREEN}done...')


def initialize():
    print(rf"""{colorama.Fore.GREEN}
 ___       __   _______   ________  ________  ________  ________  _____ ______      
|\  \     |\  \|\  ___ \ |\   __  \|\   ____\|\   __  \|\   __  \|\   _ \  _   \    
\ \  \    \ \  \ \   __/|\ \  \|\ /\ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \   
 \ \  \  __\ \  \ \  \_|/_\ \   __  \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \  
  \ \  \|\__\_\  \ \  \_|\ \ \  \|\  \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ 
   \ \____________\ \_______\ \_______\____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\
    \|____________|\|_______|\|_______|\_________\|__|     \|__|\|__|\|__|     \|__|
                                      \|_________|                                  
                                                                                        by mighty https://github.com/therealmighty
     """)
    webhook = input("Enter ur webhook > ")
    name = input("Enter a webhook name > ")
    message = input("Enter a message > ")
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('title potatohook on top LOL')
    os.system('cls' if os.name == "nt" else "clear")
    colorama.init()
    initialize()
