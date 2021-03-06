import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

df = pd.read_csv('cars.csv')
print(df)

engine = create_engine('mysql+pymysql://dev:ax2@localhost:3307/python')
with engine.connect() as conn, conn.begin():
    df.to_sql('cars', conn, if_exists='replace')
