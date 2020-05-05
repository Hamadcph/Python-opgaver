import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&K%C3%98N=TOT&ALDER=IALT&CIVILSTAND=G%2CU%2CF&Tid=2008K1%2C2020K1"

data = pd.read_csv(url, sep=';')
print(data)
gift = data.loc[data.CIVILSTAND == "Gift/separeret"]["INDHOLD"].values.tolist()
ugift = data.loc[data.CIVILSTAND == "Ugift"]["INDHOLD"].values.tolist()
fraskilt = data.loc[data.CIVILSTAND == "Fraskilt"]["INDHOLD"].values.tolist()
print("gift:", gift)
print("ugift:", ugift)
print("fraskilt:", fraskilt)
years = (2008, 2020)

indices = np.arange(len(gift))
width = 0.2

fig, ax = plt.subplots()
giftBar = ax.bar(indices, gift, width, color="r")
ugiftBar = ax.bar(indices+width, ugift, width, color="b")
fraskiltBar = ax.bar(indices-width, fraskilt, width, color="g")

ax.set_ylabel('People')
ax.set_title('Marital Status in Copenhagen, 2008, 2020')
ax.set_xticks(indices + width / 2)
ax.set_xticklabels(years)

ax.legend((giftBar[0], ugiftBar[0], fraskiltBar[0]),
          ('Gift', 'Ugift', 'Fraskilt'))

plt.show()
