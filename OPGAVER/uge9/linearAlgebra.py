import numpy as np
import pandas as pd


shoppers = np.array([[4, 2, 3, 2],
                     [2, 5, 0, 4],
                     [5, 3, 4, 5],
                     [1, 8, 9, 1]])

shop_prices = np.array([[10.50, 4],
                        [2.25, 4.5],
                        [4.5, 6.25],
                        [33.5, 20]])
R = shoppers.dot(shop_prices)

print(R)

# P1 = pd.DataFrame(shoppers).T
# Q1 = pd.DataFrame(shop_prices)
# R = P1.dot(Q1)
# print(R)
