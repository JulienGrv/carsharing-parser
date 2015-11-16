# coding: utf-8
#!/usr/bin/env python

import os
import sys
import codecs
import urllib3
import re
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
    return response.data.decode('utf-8')

##
# save html content in a file
# html - HTML content
# file_name - File name
##
def save_html(html, file_name):
    file = open(file_name + '.html', "w")
    for line in html.splitlines():
        line += u'\n'
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
def blablacar_url(origin, destination, date, limit):
   return u"https://www.blablacar.co.uk/search?fn="+origin+"&tn="+destination+"&db="+date+"&sort=trip_date&order=asc&limit="+limit

##
#
##
def get_blablacar_soup(url):
    resp = http_request(url)
    html = html_content(resp)
    resp.close()
    save_html(html, "test")
    return BeautifulSoup.BeautifulSoup(html, "lxml")

##
# 
##
def get_number_blablacar(soup):
    text = soup.find('div', 'pagination-info span3').get_text(strip=True)
    results = re.search('.+ ([0-9]+) results', text)
    if results:
        number = results.group(1)
    return number

# main
##
def main():
    print("Hello World!")
    origin = "Sens"
    destination = "Troyes"
    date = "19/11/2015"
    number = "100"
    url = blablacar_url(origin, destination, date, number)
    soup = get_blablacar_soup(url)
    number = get_number_blablacar(soup)
    if int(number) > 100:
        url = blablacar_url(origin, destination, date, number)
        print(url)
        soup = get_blablacar_soup(url)
        for p in soup.find_all('h2', 'username'):
            print(p.encode('utf-8').decode('cp1252'))
    elif int(number) > 0:
        print(url)
        for p in soup.find_all('h2', 'username'):
            print(p.encode('utf-8').decode('cp1252'))
    else:
        print("no results!")

main()
os.system("PAUSE")
