from tkinter import filedialog
import tkinter
import os
from bs4 import BeautifulSoup
import requests
import time
filepath = 'nothing'
root = tkinter.Tk()
root.withdraw()
while not (filepath.endswith('304930') or filepath.endswith('Content')):
    print('Please navigate to your Unturned workshop directory. (Directory should be named 304930)')
    filepath = filedialog.askdirectory()
    print(filepath)
    if (filepath.endswith('304930') or filepath.endswith('Content')):
        print('This is probably a workshop directory. Or at least I hope it is.')
    else:
        print('This is not an Unturned workshop directory.')
workshopmods = os.listdir(filepath)
htmlworkshop = open("unturnedworkshopitems.html","w+")
htmlworkshop.write('<!DOCTYPE html><html><head><title>Your Unturned Workshop Mods</title></head><body>')
htmlworkshop.close()
timestart = time.time()
for modid in workshopmods:
    steamurl = ('https://steamcommunity.com/workshop/filedetails/?id=' + modid)
    steampage = requests.get(steamurl)
    webdata = BeautifulSoup(steampage.text, 'lxml')
    modname = webdata.find("div", { "class" : "workshopItemTitle" }, text = True)
    if modname == None:
        print('A mod wasn\'t found: '+modid)
        htmlworkshop = open('unturnedworkshopitems.html', 'a+')
        htmlworkshop.write('<a href="#" style="color: red;">'+modid+'</a><br />')
        continue
    print(modname.text)
    htmlworkshop = open('unturnedworkshopitems.html', 'a+')
    htmlworkshop.write('<a href="'+steamurl+'">'+modname.text+' / '+modid+'</a><br />')
print('Done! All mods processed in '+str(time.time() - timestart)+' seconds.')
htmlworkshop = open('unturnedworkshopitems.html', 'a+')
htmlworkshop.write('</body></html>')
print('You can find a clickable list of your workshop items in unturnedworkshopitems.html in the folder that this script is in.')
