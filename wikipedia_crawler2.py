#!/usr/bin/env python3
'''Do not crawl the same page'''

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id = "mw-content-text").findAll("p")[0])
        print(bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries through!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encoutered a new page
                newPage = link.attrs['href']
                print("--------------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
