#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import urllib2 as ul

doc = ul.urlopen('https://www.ted.com/')
soup = bs(doc,'lxml')
#i = 1

#for link in soup.findAll('a'):
#    print i
#    i += 1
#    print link.get('href')
#    print link.string

for link in soup.body.findAll('a'):
    print link.string
    print link.get('href')
