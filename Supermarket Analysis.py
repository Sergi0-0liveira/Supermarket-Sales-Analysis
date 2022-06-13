# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:01:28 2022

@author: SergioOliveira
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('supermarket_sales.csv')
df.head()

# converting date to datetime format
df['Date'] = pd.to_datetime(df['Date'])


# setting data as the index

df.set_index('Date', inplace=True)

#calculating a few statistics
df.describe()

#UNIVARIATE Analysis
# Question 1: what does the distribution of customers ratins looks like? is it skewed?
#sns.displot(df['Rating']) 
#distplot is deprecated
#calculanting the average

#plt.axvline(x=np.mean(df['Rating']), c='red', ls ='--', label = 'mean')   
#plt.axvline(x=np.percentile(df['Rating'], 25), c='green', ls='dotted', label ="25th and 75th percentile")
#plt.axvline(x=np.percentile(df['Rating'], 75), c='green', ls='dotted')

#to display the labels
#plt.legend()

#if we want to display the remaining variables
# df.hist(figsize=(10,10))
# In order to display the above plot remove the '#'

# Question 2: Do aggregate sales numbers differ by branch?

#sns.countplot(x=df['Branch'])
#df['Branch'].value_counts()

#Question 3: Is there a relationship between gross income and customer ratings?

#sns.scatterplot(df['Rating'], df['gross income'])
#sns.regplot(df['Rating'], df['gross income'])

#is there a relation between branch and gross income?

#sns.boxplot(x=df['Branch'], y=df['gross income'])

#is there a relation between gender and gross income?
#sns.boxplot(x=df['Gender'], y=df ['gross income'])

#Is there a time trand in gross income?

#because the Date time data has several rows (the same date has several purchases) we need to group by date(index)

#sns.lineplot(x= df.groupby(df.index).mean().index, y= df.groupby(df.index).mean()['gross income'])

#cleaning removing duplicate rows
#print(df.duplicated())
#duplicated_rows = df[df.duplicated() ==True]
#sum_duplicated_rows = df.duplicated().sum()
#print(f'The number of duplicated rows is {sum_duplicated_rows} rows')
#understanding which the rows are duplicated

#print(df[df.duplicated()==True])

# to eliminate the duplicate lines you just type:

#df.drop_duplicates(inplace=True)

#understanding missing values
#print(df.isna().sum())
#print(df.isna().sum()/len(df))
#visualizing the missing values

#sns.heatmap(df.isnull(), cbar = False)

#Correlation Analysis between 2 factors

print(np.corrcoef(df['Rating'], df['gross income']))
print(round(np.corrcoef(df['Rating'], df['gross income'])[1][0],2))

#understand the correlation between all variables
print(round(df.corr(),2))

sns.heatmap(np.round(df.corr(), 2), annot=True)

print(df.head(10))