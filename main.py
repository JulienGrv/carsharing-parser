# coding: utf-8
#!/usr/bin/env python

import os
import sys
import codecs
import urllib3
import urllib.request as urllib
import certifi
import bs4 as BeautifulSoup

##
# GET http request on a url
# url - string
##
def http_request(url):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    return http.request('GET', url)

##
# retieve content of the page
# response - http request response
##
def html_content(response):
    return response.data.decode('latin-1')

##
# save html content in a file
# html - HTML content
# file_name - File name
##
def save_html(html, file_name):
    file = open(file_name + '.html', "w")
    for line in html.splitlines():
        line += '\n'
        file.write(line.encode('cp1252', errors='replace').decode('cp1252'))
    file.close()

##
# read html content in a file
# file_name - File name
##
def open_html(file_name):
    file = open(file_name + '.html', "r")
    for line in file.readlines():
        print(line)
    file.close()

##
# Blablacar link
# origin
# destination
# date
##
def blablacar_url(origin, destination, date):
   return u"https://www.blablacar.fr/search?fn="+origin+"&tn="+destination+"&db="+date+"&sort=trip_date&order=asc&limit=1000"

##
# main
##
def main():
    print("Hello World!")
    # url = u"https://www.blablacar.fr/trajets/paris/bordeaux/#?fn=Paris&fc=48.856614%7C2.352222&fcc=FR&tn=Bordeaux&tc=44.837789%7C-0.57918&tcc=FR&db=20/11/2015&sort=trip_price_euro&order=asc&limit=100"
    url = blablacar_url("Paris", "Bordeaux", "20/11/2015")
    resp = http_request(url)
    html = html_content(resp)
    resp.close()
    save_html(html, "test")
    soup = BeautifulSoup.BeautifulSoup(html, "lxml")
    for p in soup.find_all('h2', 'username'):
        print(p)
    # open_html("test")

main()
os.system("PAUSE")
