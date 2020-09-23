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
print(ps)
