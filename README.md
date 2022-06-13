# Supermarket-Sales-Analysis

In this project I performed Exploratory Data Analysis (EDA) in Python. 
Using packages such as Pandas, Numpy, Matplotlib, Seaborn etc. to conduct univariate analysis, bivariate analysis and correlation analysis.
I also used this packages to identify and handle duplicate/missing data.

Steps:
***1. reading and understanding the dataset;***

    df = pd.read_csv('supermarket_sales.csv')
    df.head()

In this case it was necessary to change the Date column to datetime data type:

    df['Date'] = pd.to_datetime(df['Date'])

and then I set the date column as the Index:

    df.set_index('Date', inplace=True)

***2. Univariate Analysys:
What does the distribution of customers ratins looks like? is it skewed?***

    sns.histplot(df['Rating']) 

![image](https://user-images.githubusercontent.com/80319492/173439533-901d2142-298f-4041-9d4e-84276be13e48.png)


Understanding the 25th percentile, the mean and the 75th percentile:

    plt.axvline(x=np.mean(df['Rating']), c='red', ls ='--', label = 'mean')   
    plt.axvline(x=np.percentile(df['Rating'], 25), c='green', ls='dotted', label ="25th and 75th percentile")
    plt.axvline(x=np.percentile(df['Rating'], 75), c='green', ls='dotted')
    plt.legend()
    
 ![image](https://user-images.githubusercontent.com/80319492/173439902-fa5489a1-5ddd-4ce6-9675-7fcb4d49a805.png)

If we want and easier and quick way to display all the variables:

    df.hist(figsize=(10,10))
  
![image](https://user-images.githubusercontent.com/80319492/173440105-6331d26f-2ffd-48e3-8b2a-24dd68e56035.png)

***3. Do aggregate sales numbers differ by branch?***

    sns.countplot(x=df['Branch'])
    df['Branch'].value_counts()

![image](https://user-images.githubusercontent.com/80319492/173441380-ddbc504d-b00a-40a0-9adf-db01df2e5ddc.png)


***4. Is there a relationship between gross income and customer ratings?

    sns.scatterplot(df['Rating'], df['gross income'])
    sns.regplot(df['Rating'], df['gross income'])

![image](https://user-images.githubusercontent.com/80319492/173441469-a4721d81-8fe7-4d10-8948-276ea1259667.png)

***5.Is there a relation between gender and gross income?

    sns.boxplot(x=df['Gender'], y=df ['gross income'])
    
 ![image](https://user-images.githubusercontent.com/80319492/173441650-4b6fbb2e-0859-4635-a176-d0cd9df9e063.png)


***6. Is there a time trend in gross income?

Because the Date time data has several rows (the same date has several purchases) we need to group by date(index)

    sns.lineplot(x= df.groupby(df.index).mean().index, y= df.groupby(df.index).mean()['gross income'])

![image](https://user-images.githubusercontent.com/80319492/173441787-7b56f8c6-e16a-4549-b293-2c079f8ed3b9.png)


***7. Cleaning removing duplicate rows

    print(df.duplicated())
    duplicated_rows = df[df.duplicated() ==True]
    sum_duplicated_rows = df.duplicated().sum()
    print(f'The number of duplicated rows is {sum_duplicated_rows} rows')

**7.1. Understanding which the rows are duplicated:

    print(df[df.duplicated()==True])
    
**7.2 To eliminate the duplicates:

    df.drop_duplicates(inplace=True)
    
    
**7.3. Get missing values or empty cells and visualizing it:

    print(df.isna().sum())
    print(df.isna().sum()/len(df))
    sns.heatmap(df.isnull(), cbar = False)

![image](https://user-images.githubusercontent.com/80319492/173442848-6836d0ff-a3e2-47ba-b02b-90416f4c59e7.png)


***8. Correlation Analysis Between 2 variables

    print(np.corrcoef(df['Rating'], df['gross income']))
    
    Output:
    [[ 1.        -0.0385905]
    [-0.0385905  1.       ]]
    
    print(round(np.corrcoef(df['Rating'], df['gross income'])[1][0],2))
    
    Output:
    -0.04
 
 ***9. Understand the correlation between all variables
 
    print(round(df.corr(),2))
    
    sns.heatmap(np.round(df.corr(), 2), annot=True)

![image](https://user-images.githubusercontent.com/80319492/173443592-5ea7430c-840b-458e-88cc-15676a9fbf7b.png)

Coorelation between 2 variable can be positive or negative. A ***positive correlation*** between two variables means both the variables move in the same direction. An increase in one variable leads to an increase in the other variable and vice versa.
**For example**, quantity and gross income have a positive correlation, which means that if one increases the other tends to increase. 
A ***negative correlation*** A negative correlation between two variables means that the variables move in opposite directions. An increase in one variable leads to a decrease in the other variable and vice versa. In this data set the negative correlations are very close to 0. However, we can assume that ***for example***, increasing the quantity of items decreases the rating given. A ***Weak/Zero correlation***  means that no correlation exists when one variable does not affect the other.

    
