import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("coffee_sales_cleaned.csv")

# Create MySQL connection
engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost:3306/coffee_sales"
)

# Upload DataFrame to MySQL
df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")
