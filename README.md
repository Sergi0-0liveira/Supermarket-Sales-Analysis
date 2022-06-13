# Supermarket-Sales-Analysis

In this project I performed Exploratory Data Analysis (EDA) in Python. 
Using packages such as Pandas, Numpy, Matplotlib, Seaborn etc. to conduct univariate analysis, bivariate analysis and correlation analysis.
I also used this packages to identify and handle duplicate/missing data.

Steps:
1. reading and understanding the dataset;

df = pd.read_csv('supermarket_sales.csv')
df.head()

#In this case it was necessary to change the Date column to datetime data type:

df['Date'] = pd.to_datetime(df['Date'])


Univariate Analysys:
Try to answer the following question: What does the distribution of customers ratins looks like? is it skewed?
