# coding: utf-8
#!/usr/bin/env python

import os
import sys
import codecs
from urllib.request import urlopen
from urllib import parse
import bs4 as BeautifulSoup


def main():
    print("Hello World!")
    url = u"https://www.blablacar.fr/trajets/paris/bordeaux/#?fn=Paris&fc=48.856614%7C2.352222&fcc=FR&tn=Bordeaux&tc=44.837789%7C-0.57918&tcc=FR&db=20/11/2015&sort=trip_price_euro&order=asc&limit=100"
    response = urlopen(url)
    html = response.read()
    response.close()
    file = open("test.html", 'w')
    for line in html.splitlines():
        line += b'\n' # line return
        file.write(line.decode('utf-8').encode('cp1252', errors='replace').decode('cp1252'))
    file.close()
    soup = BeautifulSoup.BeautifulSoup(html, "lxml")
    for p in soup.findAll('h2','username'):
        print(p)

main()
os.system("PAUSE")
