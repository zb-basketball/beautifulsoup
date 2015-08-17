#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2 as ul
from bs4 import BeautifulSoup as bs


doc = ul.urlopen('http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html')
soup = bs(doc,'lxml')

print(soup.title)
print(soup.title.string)
print(soup.title.contents)

print(soup.get_text())
