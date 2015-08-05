#!/usr/bin/env python
#-*- coding: utf-8 -*-


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p> """

soup = BeautifulSoup(html_doc,'lxml')
soup1 = BeautifulSoup(open('baidu.html'),'lxml')

print(soup1.title)
#print(soup1.findAll('a'))
#print(soup1.find_all('a'))
for link in soup1.find_all('a'):
    print(link.get('href'))
    print(link.get('id'))


print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')


print(soup.title)


print(soup.title.parent)

print(soup.title.parent.parent)

print(soup.title.name)

print(soup.title.parent.name)

print(soup.title.parent.parent.name)

print(soup.a)

print(soup.find_all('a'))

print(soup.find(id = 'link3'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.getText())

print('all tags:<<<<')
for tag in soup.find_all(True):
    print(tag.name)
