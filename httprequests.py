import urllib3
import certifi

##
# GET http request on a url
# url - string
##


def https_request(url):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    resp = http.request('GET', url)
    html = html_content(resp)
    resp.close()
    return html

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
