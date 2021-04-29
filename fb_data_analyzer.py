# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:52:59 2019

@author: adity
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentItensityAnalyzer
nltk.downloader.download('vader_lexicon')
file=''
xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_names[0])
dfs=list(dfs['Timeline'])
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="UTC+5:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])