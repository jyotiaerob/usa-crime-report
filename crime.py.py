import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
import csv



df=pd.read_csv('C:\\Users\\PrismADS\\Desktop\\crime.csv')
style.use('fivethirtyeight')

print(df.loc[:5,:])
df['Murder'].hist(bins=10)
plt.xlabel('Murder')
# frequency label
plt.ylabel('Violent')
df.plot()
plt.show()