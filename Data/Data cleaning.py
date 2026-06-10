#import libraries
import pandas as pd

df = pd.read_csv("Coffee Shop Sales.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#print(df)                              -- for general data viewing
#print(df.shape)                        -- to view number of rows and columns (here 149116, 11)
#print(df.columns)                      -- to view column names
#print(df.info())                       -- to view data types and memory usage
#print(df.isnull().sum())               -- to check number of null values in each column
#print(df['transaction_id'].unique())   -- unique values in column (here 149456)


#duplicates = df['transaction_id'].duplicated().sum()
#print(duplicates)                      -- duplicate rows (here 0)


#checking missing values
# min_id = df['transaction_id'].min()
# max_id = df['transaction_id'].max()
#
# expected = set(range(min_id, max_id + 1))
# actual = set(df['transaction_id'])
#
# missing = sorted(expected - actual)
#
# print("Number of missing IDs:", len(missing))
# print("First 20 missing IDs:", missing[:20])


#checking for spelling mistakes
# print(df['product_category'].value_counts())
# print(df['product_type'].value_counts())


#checking for missing values
#print(df['product_category'].value_counts().sum())         -- result 149116 hence okay
#print(df['product_type'].value_counts().sum())             -- result 149116 hence okay


df.to_csv("coffee_sales_cleaned.csv", index=False)
