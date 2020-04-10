# -*- coding: utf-8 -*-

"""

Created on Fri Mar  6 10:32:38 2020

/home/chris/.local/lib/python2.7/site-packages'
    ##how i orgiinally set password by db-ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Bulluck11';
    ##"insert into cardat values ( 2, 'k','m','f','d' ,'l', 7000 , 5)" 
@author: chono

"""
import requests
import MySQLdb
from bs4 import BeautifulSoup
import re
import pandas as pd

class cars:
    
    def __init__(self,url,vtype,train):
        self.url=url
        self.page=requests.get(self.url).content
        self.soup = BeautifulSoup(self.page, 'html.parser')
        self.title=self.soup.findAll('span', class_="listingTitle")
        self.price=self.soup.findAll("span", class_="cargurus-listing-search__car-blade__information__price__listing-price")
        self.location=self.soup.findAll("div", class_="srp-listing-blade-location")
        self.mileage=self.soup.findAll('p', class_="cargurus-listing-search__car-blade__information__mileage")
        self.trans=self.soup.findAll('p', class_="detailsSection transmission")
        self.color=self.soup.findAll('p', class_="detailsSection color")
        self.certified=self.soup.findAll('p', class_="detailsSection cpo")
        self.length=len(self.price)
        self.vtype=vtype
        self.titlelist=[]
        self.train=train
        for i in range(0,self.length):
            self.titlelist.append(re.findall('\n                                (.+?)\n',str(self.title[i]))[0])        

    def getcolor(self):
        colorlist=[]
        for i in range(0,self.length):
            colorlist.append(re.findall('<span>(.+?)</span>',str(self.color[i]))[0])
        return colorlist

    def getyear(self):
        yearlist=[]
        for i in range(0,self.length):
            yearlist.append(int(self.titlelist[i][0:4]))
        return yearlist

    def getmake(self):
        makelist=[]
        for i in range(0,self.length):
            makelist.append(re.findall('(?<=\s)(.*?)(?=\s)', self.titlelist[i])[0])  
        return makelist

    def getmodel(self):
        modellist=[]
        for i in range(0,self.length):
            modellist.append(re.findall('(?<=\s)(.*?)(?=\s)', self.titlelist[i])[1])  
        return modellist      

    def getprice(self):
        pricelist=[]
        for i in range(0,self.length):
            pricelist.append(float(re.findall('price">(.+?)</span>',str(self.price[i]))[0].strip("$").replace(',','')))
        return pricelist

    def getmiles(self):
        mileslist=[]
        for i in range(0,self.length):
            mileslist.append(float(re.findall('mileage">(.+?) mi</p>',str(self.mileage[i]))[0].replace(',','')))
        return mileslist         

    def gettrans(self):
        translist=[]
        for i in range(0,self.length):
            translist.append(re.findall('<span>(.+?)</span>',str(self.trans[i]))[0])
        return translist

    def getlocation(self):
        loclist=[]
        for i in range(0,self.length):
            loclist.append(re.findall('\n(.+?)\n<sp',str(self.location[i]).replace(" ",""))[0])
        return loclist 

    def checklengths(self):
        l=[len(self.location),len(self.title),len(self.price),len(self.color),len(self.trans),len(self.mileage)]
        return l
    
    def getvtype(self):
        typelist=[]
        for i in range(0,self.length):
            typelist.append(self.vtype)
        return typelist
    
    def vframe(self):
        vlist=list(zip(self.getyear(),self.getmake(),self.getmodel(),self.getvtype(),self.gettrans(),self.getmiles(),self.getprice()))
        return vlist
    
    def dbc(self):
    #inserts vframe into cardat
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
             user="root",         # your username
             passwd="Bulluck1!",  # your password
             db="cars")
        cursor=db.cursor()
        vframe=self.vframe()
        for i in range(0,self.length):
            try:
                cursor.execute("insert into cardat (year,make,model,vtype,trans,miles,price,train) values (%s,%s,%s,%s,%s,%s,%s,%s)",(vframe[i][0],vframe[i][1],vframe[i][2],vframe[i][3],vframe[i][4],vframe[i][5],vframe[i][6],self.train))
            except:
                pass
        db.commit()
        db.close()
        
    def alterdb(command):
    #alters table, insert, delete etc 
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
             user="root",         # your username
             passwd="Bulluck1!",  # your password
             db="cars")
        cursor=db.cursor()
        cursor.execute(command)
        db.commit()
        db.close()
    def querydb(command):
    #returns query results 
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
             user="root",         # your username
             passwd="Bulluck1!",  # your password
             db="cars")
        cursor=db.cursor()
        cursor.execute(command)
        a=cursor.fetchall()
        db.close()
        return pd.DataFrame(list(a))
        


        
        
