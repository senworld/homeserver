#!/usr/bin/python3

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from os import system
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG)
sleep(60)


def imagedown(url,folder):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    image = ""
    link = ""
    if("mangasee123" in url):
        image = soup.find("img", {"class": "img-fluid bottom-5"})
        link = image['src']
    elif("manganato" in url):
        image = soup.find("span", {"class": "info-image"})
        link = image.img.get('src')
    else:
        return
    with open('/mnt/Seagate_1TB/Manga/'+ folder +'/cover.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
        logging.info("Cover Updated.")



while(True):
    logging.info("---------------------------------------------------------------")
    f = open("/home/sen/Mangalinks.txt","r")
    lines=f.read().splitlines()
    for i in range(0,len(lines),2):
        logging.info(lines[i+1]+"\n")
        if(lines[i]==" " or lines[i]==""):
            break
        if(lines[i][0]=="#"):
        	 continue
        system('docker exec mangapy manga-py -d /home/manga --global-progress --no-webp --cbz --user-agent "Chrome" --rename-pages --name "'+lines[i+1]+'" '+lines[i])
        if(not(Path('/mnt/Seagate_1TB/Manga/'+ lines[i+1] +'/cover.jpg').is_file())):
            lines[i] = lines[i].split(" ",1)
            lines[i] = lines[i][0]
            imagedown(lines[i],lines[i+1])
    f.close()
    logging.info("Checking back in 2 hour...")
    sleep(7200)

