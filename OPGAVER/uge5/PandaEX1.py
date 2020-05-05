import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# opgave 5a What is the change in pct of divorced danes from 2008 to 2020?

url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&K%C3%98N=1%2C2&ALDER=IALT&CIVILSTAND=G&Tid=2008K1%2C2008K2%2C2008K3%2C2008K4%2C2020K1"
data = pd.read_csv(url, sep=';')

pct2008 = data['INDHOLD'][0]/data['INDHOLD'][1]
pct2020 = data['INDHOLD'][2]/data['INDHOLD'][3]
pct_increase = pct2020/pct2008*100-100
print('increase is: {}%'.format(pct_increase))

# opgave 5b
url2 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1&CIVILSTAND=TOT%2CU&K%C3%98N=TOT&OMR%C3%85DE=101%2C851%2C561%2C461%2C751&ALDER=IALT"
data2 = pd.read_csv(url2, sep=';')

not_married_pct = {data2['OMRÅDE'][not_married][4:]: data2['INDHOLD'][not_married]/data2['INDHOLD']
                   [all_people]*100 for not_married, all_people in zip(range(5, 10), range(0, 5))}

result = {}
for not_married, all_people in zip(range(5, 10), range(0, 5)):
    pct_not_married = data2['INDHOLD'][not_married] / \
        data2['INDHOLD'][all_people]*100
    city = data2['OMRÅDE'][not_married][4:]
    result[city] = pct_not_married
print(sorted(not_married_pct, key=not_married_pct.get, reverse=True))

