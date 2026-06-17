#import libraries
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("Coffee Shop Sales.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df)                              #-- for general data viewing
print(df.shape)                        #-- to view number of rows and columns (here 149116, 11)
print(df.columns)                      #-- to view column names
print(df.info())                       #-- to view data types and memory usage
print(df.isnull().sum())               #-- to check number of null values in each column
print(df['transaction_id'].unique())   #-- unique values in column (here 149456)


duplicates = df['transaction_id'].duplicated().sum()
print(duplicates)                      #-- duplicate rows (here 0)


#checking missing values
df.isnull().sum()
df.isna().sum()



#checking for spelling mistakes
print(df['product_category'].value_counts())
print(df['product_type'].value_counts())


#checking for missing values
print(df['product_category'].value_counts().sum())         #-- result 149116 hence okay
print(df['product_type'].value_counts().sum())             #-- result 149116 hence okay


# Convert date
df['transaction_date'] = pd.to_datetime(
    df['transaction_date'],
    format='%d-%m-%Y'
)

# Convert time
df['transaction_time'] = pd.to_datetime(
    df['transaction_time'],
    format='%H:%M:%S'
)
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

print(df.dtypes)

df.to_csv("cleaned_data.csv", index=False)

# now connecting my file to MySQL server
engine = create_engine("mysql+pymysql://root:password@localhost:3306/coffee_sales")
df.to_sql(
    name='coffee_sales',
    con=engine,
    if_exists='replace',
    index=False
)
print("done!")


