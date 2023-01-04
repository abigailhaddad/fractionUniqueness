# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:28:30 2023

@author: abiga
"""
import pandas as pd

listOfLists=[]
for i in range(1, 10001):
    for j in range(0, 10000):
        if j>=i:
            listOfLists.append([i, j])
        
df=pd.DataFrame(listOfLists)
df.columns=["Numerator", "Denominator"]

df['Percent']=df['Numerator']/df['Denominator']

listofAnswers=[]
for places in range(1, 7):
    var_name=f"percent_round_{places}"
    df[var_name]=df['Percent'].round(places)
    for denominator_limit in [100, 200, 500, 1000, 2000, 5000, 10000]:
        subset=df.loc[df['Denominator']<=denominator_limit]
        values=subset[var_name].value_counts().value_counts()
        try:
            identified_perfect=values.loc[1]/len(subset)
        except:
            identified_perfect=0
        listofAnswers.append([places, denominator_limit, identified_perfect])
    
answers=pd.DataFrame(listofAnswers)
answers.columns=['Rounding Digits', 'Denominator Maximum', 'Percentage Identified Perfectly']

pivoted=pd.pivot(answers, index='Rounding Digits', columns='Denominator Maximum', values='Percentage Identified Perfectly')

