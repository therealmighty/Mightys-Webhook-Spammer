import time
import requests
import pyfiglet
from colorama import Fore, Style, init

init()

text = pyfiglet.figlet_format("webhook spam")

print(Fore.GREEN + text + Style.RESET_ALL)

msg = input("Please Insert webhook Spam Message: ")
webhook = input("Please Insert webhook URL: ")

def spam(msg, webhook):
    for i in range(30):
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()

counts = 1
while counts == 1:
    spam(msg, webhook)
