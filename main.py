import pandas as pd
import numpy as np

dat = pd.read_csv('Fishing.csv')
dat['log_income'] = dat.loc[:, 'income'].apply(np.log)
f = lambda x: abs(x - x)

# dat['pdiff'] = dat[['price', 'pbeach']].apply(f, axis=1)
dat['pdiff2'] = abs(dat['price'] - dat['pbeach'])

for name, data in dat.groupby("mode"):
    data.to_csv(f"{name}" + '.csv')

# print(dat)
