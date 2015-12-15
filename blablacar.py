import bs4 as BeautifulSoup
import re
from urllib.parse import quote
from httprequests import *

##
# Blablacar link
# origin
# destination
# date
##


def get_blablacar_url(origin, destination, date, limit):
    origin = quote(origin)
    destination = quote(destination)
    return u"https://www.blablacar.co.uk/search?db=" + date + "&fn=" + origin + "&tn=" + destination + "&sort=trip_date&order=asc&limit=" + limit + "&page=1"

##
#
##


def get_blablacar_soup(url):
    html = https_request(url)
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
