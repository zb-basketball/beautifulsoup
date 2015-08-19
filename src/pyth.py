#!/usr/bin/python
# -*- coding: utf-8  -*-

import urllib2
from bs4 import BeautifulSoup
from operator import itemgetter


if __name__ == '__main__':
    a=[9,5,6,7,3,2,4,5,1,1,5,4,2,3,7,6,8]
    d={}
    
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    
    for i in d:
        if d[i] == 1:
            print i

    print d


    '''for i in range(10,20):
        if i == 15:
            print 'break'
            break
        print i,
    else:
        print
        print 20
    '''
    print d
