import pandas as pd

# Создание фрейма данных

df = pd.DataFrame({'Date': ['11/8/2011', '11/9/2011', '11/10/2011',

                            '11/11/2011', '11/12/2011'],

                   'Event': ['Music', 'Poetry', 'Music', 'Music', 'Poetry']})

# Распечатайте фрейм данных

print(df)
df['Price'] = [1500 if x == 'Music' else 800 for x in df['Event']]

# Распечатать DataFrame

print(df)