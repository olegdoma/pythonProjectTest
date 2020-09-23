import pandas as pd
import numpy as np

ps = pd.read_csv("extraversion.csv", encoding="UTF-8")


def f(x):
    return x.replace(' ', '')


ps_columns = ps.columns.values.tolist()
ps_columns_Q = ps_columns[4:]
ps_columns_new_Q = list(map(f, ps_columns_Q))
ps_columns_without_Q = ps_columns[:4]
ps_columns_new = ps_columns_without_Q + ps_columns_new_Q
ps.columns = ps_columns_new

extra_yes = ps[['Q1', 'Q3', 'Q8', 'Q10', 'Q13', 'Q17', 'Q22', 'Q25', 'Q27', 'Q39', 'Q44', 'Q46', 'Q49', 'Q53', 'Q56']]
extra_no = ps[['Q5', 'Q15', 'Q20', 'Q29', 'Q32', 'Q34', 'Q37', 'Q41', 'Q51']]

# print(extra_yes)
new_extra_yes = extra_yes.isin(['Да'])
# print(new_extra_yes)

extra_yes_sum = new_extra_yes.sum(axis=1, numeric_only=True)
# print(extra_yes_sum)

new_extra_no = extra_no.isin(['Нет'])
extra_no_sum = new_extra_no.sum(axis=1, numeric_only=True)

ps['extra'] = extra_yes_sum + extra_no_sum

ps['female'] = 0
ps['female'] = ps.sex.eq('Женский').astype(int)

pure = ps[((ps['volunteer'] == 'Да') & (ps['extra'] > 15)) | ((ps['volunteer'] == 'Нет') & (ps['extra'] < 15))]

sum_yes = (pure.volunteer == 'Да').sum()
sum_no = (pure.volunteer == 'Нет').sum()

print(pure)

max_extra = pure['extra'].max()
min_extra = pure['extra'].min()
mean_extra = pure['extra'].mean()
median_extra = pure['extra'].median()
# print(max_extra)
# print(min_extra)
# print(mean_extra)
# print(median_extra)

m = max(median_extra, mean_extra)
pure['high'] = [1 if x > m else 0 for x in pure['extra']]

# for x in pure['extra']:
#     if x > m:
#         pure.loc[x, 'high'] = 1
#     else:
#         pure.loc[x, 'high'] = 0
print(pure)
