from colorama.ansi import Fore
import requests
import json
import os
import colorama
from colorama import Fore, Back, Style

with open('config.json', 'r') as cf:
   data = json.loads(cf.read())
   NAME = data['name']
   AVATAR = data['avatar']
   MESSAGE = data['content']
   EMBED = data['embeds']
   WEBHOOK = data['url']
   WEBHOOK1 = data['url']
   HOWMANY = data['howmany']

def clear():
   os.system('cls')

def banner():
   print(f''' {Fore.RED}
     ______                                                                      
 /      \                                                                     
|  $$$$$$\  ______    ______   ______ ____   ______ ____    ______    ______  
| $$___\$$ /      \  |      \ |      \    \ |      \    \  /      \  /      \ 
 \$$    \ |  $$$$$$\  \$$$$$$\| $$$$$$\$$$$\| $$$$$$\$$$$\|  $$$$$$\|  $$$$$$\
 _\$$$$$$\| $$  | $$ /      $$| $$ | $$ | $$| $$ | $$ | $$| $$    $$| $$   \$$
|  \__| $$| $$__/ $$|  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$| $$$$$$$$| $$      
 \$$    $$| $$    $$ \$$    $$| $$ | $$ | $$| $$ | $$ | $$ \$$     \| $$      
  \$$$$$$ | $$$$$$$   \$$$$$$$ \$$  \$$  \$$ \$$  \$$  \$$  \$$$$$$$ \$$      
          | $$                                                                
          | $$                                                                
           \$$                                                                
                                                                                        {Fore.GREEN} Made by Sync#5666 ''')

def spam():

   while True:
      try:
         load = {"content": MESSAGE, "embeds": EMBED, "username": NAME, "avatar": AVATAR}
         r = requests.post(WEBHOOK, json=load)

         if r.status_code == 429:
            print(f'{Fore.YELLOW} Rate limit.')

      except:
         print(f'{Fore.RED} could not send the message.')
         pass

if __name__ == "__main__":
   print('Sending messages.')
   banner()
   spam()