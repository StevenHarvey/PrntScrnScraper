from random import randint, choice
from fake_useragent import UserAgent
import shutil
import os
import datetime
import time
import requests
from bs4 import BeautifulSoup
global baseurl
baseurl = "https://prnt.sc/"
times = (str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second))
global fileo
fileo = ("\\"+times)
os.mkdir((r"Output"+fileo))
global AL
AL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
op = int(input("How many Pics?(1-100): "))
if op < 1010:
    i = 0
    while i < op:
        numbers = str(randint(1000, 10000))
        letters = str(choice(AL))+str(choice(AL))
        URL = str(baseurl)+letters+numbers
        result = requests.get(URL, headers={'User-Agent': 'ua.chrome'})
        if result.status_code == 200:
            soup = BeautifulSoup(result.content, "html.parser")
            mydivs = soup.find("div", {"class": "image-container image__pic js-image-pic"})
            container = str(mydivs)
            foo = ((container.split("src=")[1].replace("\"", " ")).split()[0])
            if "//st.prntscr.com/" in foo:
                print('error running - doing new call')
            else:
                r = requests.get(foo, stream=True)
                if r.status_code == 200:
                    with open((r"C:\Users\nolan\Documents\Python\Output"+fileo+"\\"+letters+numbers+".jpg"), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)    
                i += 1
else:
    print("Error - TOO MANY PICS!\nExiting in 5")
    time.sleep(5)
