# coding: utf-8
#!/usr/bin/env python

import os
import sys
import codecs
from urllib.request import urlopen
from urllib import parse
import httplib2
import bs4 as BeautifulSoup


def main():
    print("Hello World!")
    url = u"https://www.blablacar.fr/trajets/paris/bordeaux/#?fn=Paris&fc=48.856614%7C2.352222&fcc=FR&tn=Bordeaux&tc=44.837789%7C-0.57918&tcc=FR&db=20/11/2015&sort=trip_price_euro&order=asc&limit=100"
    http = httplib2.Http(".cache")
    resp, content = http.request(url, "GET")
    # str_content = content.decode('utf-8')
    # print(str_content)
    # print(url)
    # html = urlopen(url).read()
    lines = content.splitlines()
    panda=b""
    for line in lines:
        panda += line.decode('utf-8').encode('cp1252', errors='replace')
    soup = BeautifulSoup.BeautifulSoup(panda, "html.parser")
    # soup = BeautifulSoup.BeautifulSoup(html[1], "html.parser")
    f = open("test.html", 'w+')
    # u = urlopen(url)
    # f.write(u.read().decode('utf-8'))
    # for line in lines:
        # print(line.decode('utf-8').encode('cp1252', errors='replace').decode('cp1252'))
    for line in lines:
        # print(line)
        f.write(line.decode('utf-8').encode('cp1252', errors='replace').decode('cp1252'))
    f.close()
    for p in soup.findAll('h2','username'):
        print(p)

main()
os.system("PAUSE")
