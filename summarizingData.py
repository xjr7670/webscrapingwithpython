#!/usr/bin/env python3

import re
import string
import operator
from urllib.request import urlopen
from bs4 import BeautifulSoup

def cleanInput(content):
    content = re.sub('\n+', " ", content).lower()
    content = re.sub('\[[0-9]*\]', "", content)
    content = re.sub(' +', " ", content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    cleanedInput = []
    content = content.split(' ')
    for item in content:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanedInput.append(item)
    return cleanedInput


def ngrams(content, n):
    content = cleanInput(content)
    output = {}
    for i in range(len(content)-n+1):
        ngramTemp = " ".join(content[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen("http://www.pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
#bsObj = BeautifulSoup(html, 'lxml')
#content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)
#ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
#print(ngrams)
#print("2-grams count is: " + str(len(ngrams)))
