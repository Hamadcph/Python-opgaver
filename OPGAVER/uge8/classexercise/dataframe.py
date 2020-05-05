import pandas as pd
import pymysql
# sqlalchemy helped convert strings to dates seamlessly
from sqlalchemy import create_engine

cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db='python')
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/python'
engine = create_engine(con_str)
df = pd.DataFrame({'make': ['toyota', 'audi', 'citroen'],
                   'model': ['up', 'a6', 'c3'],
                   'year': ['2018', '2011', '2019'],
                   'price': ['123000', '85000', '143000']})

#df = df.applymap(str)
df.to_sql('cars', con=engine, if_exists='append', index=False)
print(df.dtypes)
