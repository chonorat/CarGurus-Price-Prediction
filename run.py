# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from cars import cars
from scrapecardata import getdatafromsite
from scrapecardata import gettraindatafromsite
from scrapecardata import nametranstype
from cardataformat import cardataformat


#getdatafromsite()
#gettraindatafromsite()
#nametranstype()
data=cardataformat()
print(data.stats('traindata')['makeavg'])
print(data.stats('traindata')['typeavg'])
print(data.stats('traindata')['luxavg'])
print(data.stats('traindata')['nonluxavg'])
data.formatandsave()