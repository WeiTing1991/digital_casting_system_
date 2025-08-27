import csv
import os

import matplotlib.pyplot as plt

#import pandas as pd

x = [i for i in range(10)]
y = [i*2 for i in range (10)]


HERE = os.path.dirname(__file__)
HOME = os.path.abspath(os.path.join(HERE, "../../../"))
DATA = os.path.abspath(os.path.join(HOME, "data/csv"))
CSV_DIR = os.path.abspath(os.path.join(DATA, "20221028_50_agg_test.csv"))
print(CSV_DIR)

with open(CSV_DIR) as f:
    lines = csv.reader(f, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y)

plt.title('Inline_mixer', fontsize = 10)
#plt.grid()
plt.legend()
plt.show()
