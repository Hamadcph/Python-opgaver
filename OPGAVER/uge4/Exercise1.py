import numpy as np
import matplotlib.pyplot as plt

# opgave 3


def number_of_people_per_neighbourhood(n, mask):
    dd = bef_stats_df

    all_people_in_given_n = dd[mask & (dd[:, 1] == n)]
    # index 4 is no of 'PERSONER'
    sum_of_people = all_people_in_given_n[:, 4].sum()
    return sum_of_people


filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)

dd = bef_stats_df
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}

all_mask = (dd[:, 0] == 2015) & (dd[:, 3] == 5100)

all = np.array([number_of_people_per_neighbourhood(
    n, all_mask) for n in neighb.keys()])
print(all)

# opgave 4
# plt.bar(neighb.keys(), all)
# plt.xlabel("neighb", fontsize=14)
# plt.ylabel("amount of people", fontsize=14)
# plt.show()

# opgave 5
mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & (dd[:, 3] == 5100)
print(dd[mask])
print(np.sum(dd[mask][:, 4]))

# opgave 6
# 5120	Sverige
# 5104	Finland
# 5110	Norge
Sverige_mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & (dd[:, 3] == 5120)
print(np.sum(dd[Sverige_mask][:, 4]))
Norge_mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & (dd[:, 3] == 5110)
print(np.sum(dd[Norge_mask][:, 4]))
Finland_mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & (dd[:, 3] == 5104)
print(np.sum(dd[Finland_mask][:, 4]))

# opgave 7
