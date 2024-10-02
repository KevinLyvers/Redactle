# creates a dataframe with words from wordsAlpha.txt and initializes group columns to 0
import pandas as pd

# read the words from wordsAlpha.txt
with open('wordsAlpha.txt', 'r') as f:
    words = f.read().split(", ")
    
# make sure all words are interpted as strings
words = [str(word) for word in words]

# make a simple dataframe with words as the only column
df = pd.DataFrame(words, columns=['words'])

# add a column with the group numbers initalized at 0
df['g1'] = 0
df['g2'] = 0
df['g3'] = 0
df['g4'] = 0
df['g5'] = 0
df['g6'] = 0
df['g7'] = 0
df['g8'] = 0
df['g9'] = 0
df['g10'] = 0
df['g11'] = 0

# import os

# num = 1
# # get all files in numr folder
# arr = os.listdir(str(num) + 'r')
# for i, file in enumerate(arr[:10]):
#     print(f"Processing file {file}")
#     print(f"Processing file {i}")
#     with open(str(num) + 'r/' + file, 'r') as f:
#         text = f.read()[1:]
#         words = text.split(", ")

#         for word in words:
#             if word in df['words'].values:
#                 df.loc[df['words'] == word, 'g1'] += 1 

# print(df)

# save to csv
df.to_csv('out.csv', index=False)  
