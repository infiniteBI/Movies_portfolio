#import labraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure


matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

#to adjusts the confirguration of the plot we will create.
# read the data

df = pd.read_csv('movies.csv')

#let's take a look at the data

df.head() 

#check is there is missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col,pct_missing))
       
#let's drop the missing data
df_new_data= df
df_new_data.dropna(inplace=True)
#let's see the data types
print(df.dtypes)

for col in df_new_data.columns:
    pct_missing = np.mean(df_new_data[col].isnull())
    print('{} - {}%'.format(col,pct_missing))
#change column data type
df_new_data['budget'] = df_new_data['budget'].astype('int64')
df_new_data['gross']= df_new_data['gross'].astype('int64')

#df_new_data.dtypes()

#let's drop duplicate

df_new_data.drop_duplicates()

#let's see bugdet vs gross

plt.scatter(x='budget',y='gross',data=df_new_data )
plt.show()

sns.regplot(x='gross', y='budget', data=df_new_data)
plt.show()

sns.regplot(x='score', y='gross', data=df_new_data)
#let's see the correlation between budget and gross

corr1 = df_new_data['budget'].corr(df_new_data['gross'])

corr2 = df_new_data['score'].corr(df_new_data['gross'])
corr1
corr2

corr3 = df_new_data.corr(method= 'pearson')
corr3

#let's assign a ranom number to all object column and see the correlation
corr4 =  df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(corr4, annot = True)

plt.show()
corr_pairs = corr4.unstack().sort_values(kind='quicksort')
corr_pairs = corr_pairs[abs(corr_pairs) > 0.5]
print(corr_pairs)

#let's show the top 10 companies
company_gross= df_new_data.groupby('company')[['gross']].sum()
company_gross_sorted= company_gross.sort_values(by='gross',ascending=False)[:10]
print(company_gross_sorted)

#let's show the top company by year and gross

df_new_data['Year_correct']= df_new_data['released'].astype(str).str[:4]

print(df_new_data['year'])
Year_Gross= df_new_data.groupby(['company','year'])[['gross']].sum()
Year_Gross_sorted= Year_Gross.sort_values(by='gross',ascending=False)[:10]

print(Year_Gross_sorted)

#Let's see the ratings

sns.stripplot(x="rating", y="gross", data=df_new_data)