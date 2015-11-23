# coding: utf-8
#!/usr/bin/env python

import os
import sys
import codecs
import urllib3
import re
import certifi
import bs4 as BeautifulSoup
import json

##
# GET http request on a url
# url - string
##
def https_request(url):
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
def get_blablacar_url(origin, destination, date, limit):
   # return u"https://www.blablacar.co.uk/search?fn="+origin+"&tn="+destination+"&db="+date+"&sort=trip_date&order=asc&limit="+limit
   # return u"https://www.blablacar.co.uk/search?fn="+origin+"&tn="+destination+"&db="+date+"&sort=trip_date&order=asc&limit=10"
   return u"https://www.blablacar.co.uk/ride-sharing/london/birmingham/#?fn=London%2C+UK&fc=51.5073509%7C-0.1277583&fcc=GB&tn=Birmingham%2C+UK&tc=52.486243%7C-1.890401&tcc=GB&db=27%2F11%2F2015&sort=trip_date&order=asc&limit=10&page=1"

##
#
##
def get_blablacar_soup(url):
    resp = https_request(url)
    html = html_content(resp)
    resp.close()
    save_html(html, "blablacar")
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

def blablacar_search(origin, destination, date):
    number = "100"
    url = get_blablacar_url(origin, destination, date, number)
    soup = get_blablacar_soup(url)
    number = get_number_blablacar(soup)
    if int(number) > 100:
        url = get_blablacar_url(origin, destination, date, number)
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
    pass

def get_liftshare_url(origin, destination, date):
    origin = re.sub(', ', "-", origin).lower()
    destination = re.sub(', ', "-", destination).lower()
    date = re.sub('/', "-", date)
    return u"https://liftshare.com/uk/search/"+origin+"/"+destination+"/"+date

def get_liftshare_soup(url):
    resp = https_request(url)
    html = html_content(resp)
    resp.close()
    results = re.search(r'<script type="application\/ld\+json">\r\n(.*)\r\n</script>', html, re.DOTALL)
    if results:
        json_input = results.group(1)
        # print(json_input.encode('utf-8').decode('cp1252'))
    save_html(html, "liftshare")
    return BeautifulSoup.BeautifulSoup(html, "lxml"), json_input

def liftshare_search(origin, destination, date):
    url = get_liftshare_url(origin, destination, date)
    soup, json_input = get_liftshare_soup(url)
    # print(json_input.encode('utf-8').decode('cp1252'))
    parsed_json = json.loads(json_input)
    print(url)
    for offer in parsed_json['@graph']:
        print(offer['name'].encode('utf-8').decode('cp1252'))
        print(offer['startDate'].encode('utf-8').decode('cp1252'))
    pass

# main
##
def main():
    print("Hello World!")
    blablacar_search("London, UK", "Birmingham, UK", "27/11/2015")
    liftshare_search("London, UK", "Birmingham, UK", "27/11/15")
    pass

main()
os.system("PAUSE")
