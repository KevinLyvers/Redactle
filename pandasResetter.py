# reset all of out.csv files to 0

import pandas as pd

# take in out.csv
df = pd.read_csv('outRatio.csv')

# reset all of the g columns to 0
for i in range(1, 12):
    df[f'gmath{i}'] = 0

# save to csv
df.to_csv('out.csv', index=False)