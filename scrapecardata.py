#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:02:18 2020

@author: chris
"""
from cars import cars


#cities=[79936,60629,90650,90011,11220,90650,75052,60804,30301,33103,48127,83701,21201,40018,22434,36525,'08201',72701,53201,77001,37011,98101,55111,43004,28105]


body =	{
  6: "sedan",
  7: "suv",
  3: "hatch",
  1:"conv",
  8:"van",
  4:"minivan",
  5:"pickup",
  0:"coupe",
  9:"wagon"
}

def getdatafromsite():
    cities=[79936,60629,90650,90011,11220,90650,75052,60804,30301,33103,48127,83701,21201,40018,22434,36525,'08201',72701,53201,77001,37011,98101,55111,43004,28105]
    for c in cities:
        print(c)
        for k in body:
            for i in range(0,50):  
                try:
                    j=cars("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip="+str(c)+"&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg"+str(k)+"&showNegotiable=true&sourceContext=carGurusHomePageModel&distance=50#resultsPage="+str(i),body.get(k),1)
                    j.dbc()
                except:
                    pass

            
            
            
def gettraindatafromsite():

    cities=[10001,12084,90650,48127]
    for c in cities:
        print(c)
        for k in body:
            for i in range(0,50):     
                try:
                    j=cars("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip="+str(c)+"&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg"+str(k)+"&showNegotiable=true&sourceContext=carGurusHomePageModel&distance=50#resultsPage="+str(i),body.get(k),0)
                    j.dbc()
                except:
                    pass
                
        
def nametranstype():
    cars.alterdb("update cardat set trans='auto' where trans like '%automatic%'")
    cars.alterdb("update cardat set trans='manual' where trans like '%manual%'")
    cars.alterdb("update cardat set trans='auto' where trans != 'auto' and trans !='manual'")
    
    

