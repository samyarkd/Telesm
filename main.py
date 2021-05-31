from pyrogram import *
from pyfiglet import figlet_format
from colorama import init, Fore
import urllib
from termcolor import cprint 
import random
import time
import sys


init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX #Green
r = Fore.LIGHTRED_EX #RED
w = Fore.WHITE
cy = Fore.CYAN #LIGHTBLUE
ye = Fore.LIGHTYELLOW_EX
colors = [lg, r, w, cy, ye]




def main(cid):
    try:
        for user in app.iter_chat_members(chat_id= cid):
            x = user.user.id
            with open('members.txt', 'a') as file:
                sys.stdout.write('\r' + f'{lg} {x} {n}')
                file.write(str(x) + '\n')
                file.close()
        sys.stdout.write('\r' + f"{lg} members count : {app.get_chat_members_count(cid)} {n} \n {ye}")
    
    except Exception as e:
        
        print(f'{ye}chat ID is not valid ')

#app.start()
wt = f"{r} WELCOME TO SAMYAR's{cy} TeleSm BOT {n}"
wt = wt.center(92, '*')
print(wt)



init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected



cprint(figlet_format('SAMY BR', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
print(f'{r}--->          {ye} Wich one !! ?{n}')

print(f'{r}   |')
print(f'{r}   ---> {lg}[1]{n} Create session ')
print(f'{r}   |')
print(f'{r}   ---> {lg}[2]{n} Get group and supergroup members name and id ')
print(f'{r}   |')
print(f'{r}____<3____{n}{ye}')
print(' ')
while True:

    wv = input('>>> ')
    try:
    
        if int(wv) == 1:
            print(f'{cy} if you want create a new session plz go to https://my.telegram.org/ \n and enter your telegram info to get{r} API_ID {n}{cy} and {n}{r} API_HASH {n}{cy} To run the tool.{n}')
            print(f"{r}")
            xc = input('Enter session name :) ')
            try:
                api_id = input('Enter api id: ')
                api_id = int(api_id)
                api_hash = input('Enter api hash: ')
                app = Client(str(xc), api_id, api_hash)
                app.start()
                app.stop()
                print(f'{lg}session created successfully !{n}')
            except Exception as e:
                print(f'session failed, Check you data :(')


        elif int(wv) == 2:
            try:
                print(f'{r} enteryour session name you have created in previous step ')
                sn = input(" >>>>> ")
                app = Client(session_name= sn)
                app.start()
                print(f'{cy} you can easily get chat members name and id in one txt file \n you just need the chat id !! {n}{r}')
                cid = input('Enter chat id or link(t.me/CHAT): ')
                try:
                    cid = int(cid)
                    main(cid)
                    app.stop()
                except Exception as e:
                    cid = cid.lower()  
                    try:
                        reid = cid.replace('t.me/', '')
                        try:
                            reid = reid.replace('https://', '') 
                            print(reid)
                        except Exception as e:
                            pass
                        
                    except Exception as e:
                        reid = cid.replace('https://t.me/', '')
                    

                    app.start()
                    main(reid)
                    app.stop()
                    

            except Exception as e:
                print(f'{cy}There is no session with this name (you can create one in step [1]){n}{ye}')

        else: print(f'{ye} enter one of the above options :(')
  
    except Exception as e:
        print(f'{ye} enter one of the above options :(')
