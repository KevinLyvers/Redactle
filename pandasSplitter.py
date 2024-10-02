import pandas as pd

# read in out.csv

df = pd.read_csv('out.csv')

# add up each row and store in a new column exluding the first column
df['sum'] = df.iloc[:, 1:].sum(axis=1)

# sort the dataframe by the sum column
df = df.sort_values(by='sum', ascending=False)

# save the new dataframe to a new csv
df.to_csv('sum.csv', index=False)