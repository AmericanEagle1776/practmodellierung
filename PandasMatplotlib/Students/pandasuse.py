import pandas as pd

import pandas as pd

df = pd.read_csv('data.csv', sep=';', header = 0, decimal=',', na_values ='-', index_col = 0)

c = df.mean()
d = df.mode()
a = df.groupby('Identifier').mean()
b = df['A'].where(df['Classifier'] == 1.0).value_counts()
