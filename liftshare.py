import json
import bs4 as BeautifulSoup
import re
from httprequests import *


def get_liftshare_url(origin, destination, date):
    origin = re.sub(', ', "-", origin).lower()
    destination = re.sub(', ', "-", destination).lower()
    date = re.sub('/', "-", date)
    return u"https://liftshare.com/uk/search/" + origin + "/" + destination + "/" + date


def get_liftshare_soup(url):
    html = https_request(url)
    results = re.search(
        r'<script type="application\/ld\+json">\r\n(.*)\r\n</script>', html, re.DOTALL)
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
