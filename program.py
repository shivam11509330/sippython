# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:58:45 2019

@author: aa
"""

import pandas as pd
test=pd.read_csv('C:\\Users\\aa\\Desktop\\P03_30.csv')
test.head()
p3.columns
test.Euros.value_counts()
test.Euros.value_counts().head(5)
test.Euros.head(5).plot(kind='bar')


