#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:12:20 2020

@author: chris
"""



import numpy as np
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from plotnine import *
from plotnine.data import mpg
from sklearn.linear_model import LinearRegression
from cars import cars
pd.options.display.max_columns = 500


class cardataformat:
    def __init__(self):
            self.traindata=cars.querydb("select c2.*,l.lux from lux l, cardat c2 \
                 where c2.make=l.brand and train=1 and c2.make in( \
                                                                          select c.make \
                                                                          from cardat c \
                                                                          group by c.make \
                                                                          having count(c.make)>40);")
            self.testdata=cars.querydb("select c2.*,l.lux from lux l, cardat c2 \
                 where c2.make=l.brand and train=0 and c2.make in( \
                                                                          select c.make \
                                                                          from cardat c \
                                                                          group by c.make \
                                                                      having count(c.make)>40);")
            
            self.testdata.columns=['year','make','model','type','trans','miles','price','train','lux']
            self.traindata.columns=['year','make','model','type','trans','miles','price','train','lux']
            self.testdata['makemod']=self.testdata.make+self.testdata.model
            self.traindata['makemod']=self.traindata.make+self.traindata.model
    def stats(self,testortrain):
            #descriptive stats
            if testortrain=='traindata': data=self.traindata
            else : data=self.testdata
            makeavg=data.groupby("make").mean().sort_values(by='price').price
            makemodavg=data.groupby('makemod').mean().price
            luxavg=np.mean(data[data["lux"]==1])
            nonluxavg=np.mean(data[data["lux"]==0])
            typeavg=data.groupby("type").mean().sort_values(by='price').price
            transavg=data.groupby("trans").mean().price
            statdict={'makeavg':makeavg,'luxavg':luxavg,'nonluxavg':nonluxavg,'typeavg':typeavg,'transavg':transavg,'makemodavg':makemodavg}
            return statdict
        
        
        
        
    def formatandsave(self):
        datas=[self.testdata,self.traindata]
        formatteddatas=[]
        for n,data in enumerate(datas):
            
            if n==0: name='testdata'
            else : name='traindata'
            
            #quantify make variable
            makedict={}
            makeavg=self.stats(name)["makeavg"]
            for i in range(0,len(makeavg)):
                makedict.update({makeavg.index[i]:makeavg[i]})
                data["makeavg"]=data["make"].map(makedict)
                
            
            #create type variables
            typedict={}
            typeavg=self.stats(name)["typeavg"]
            for i in range(0,len(typeavg)):
                typedict.update({typeavg.index[i]:i})
                data["typecode"]=data["type"].map(typedict)
            
            #create trans variable
            transdict={"auto":0,"manual":1}
            data["transcode"]=data["trans"].map(transdict)
            
            
            #quantify make-model variable
            makemodeldict={}
            makemodavg=self.stats(name)["makemodavg"]
            for i in range(0,len(makemodavg)):
                makemodeldict.update({makemodavg.index[i]:makemodavg[i]})
                data["makemodavg"]=data['makemod'].map(makemodeldict)
            
            #save
            carclean=data.iloc[:,[0,1,2,3,4,5,8,6,10,13,11,12]]
            carclean.to_csv ('/home/chris/Desktop/carproject/personal project/rcar'+name+'.csv', index = False, header=True)
            formatteddatas.append(carclean)
        return data
        
        
        
