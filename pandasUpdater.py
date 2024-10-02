# takes in freq text files and adds the frequncies to the out.csv file

import os
import pandas as pd

types = {'words': str, 'g1': int, 'g2': int, 'g3': int, 'g4': int, 'g5': int, 'g6': int, 'g7': int, 'g8': int, 'g9': int, 'g10': int, 'g11': int}

files = os.listdir('freqs')
df = pd.read_csv('out.csv', dtype=types)

nowords = []


def binary_search_pandas(df, target):
    # df is in order
    
    target = str(target)
    #print(target)
   
    
    left = 0
    right = len(df) - 1
    mid = (left + right) // 2
    
    while left <= right:
        #print("df words: ", df['words'][mid])
        mid = (left + right) // 2
        if str(df['words'][mid]) == target:
            return mid
        elif str(df['words'][mid]) < target:
            left = mid + 1
        else:
            right = mid - 1
    
    
    return -1
    

for i in range(1, 12):
    print(f"Processing folder {i}")
    files = os.listdir(str(i) + 'r')
    for j, file in enumerate(files):
        if j % 100 == 0:
            # save to csv
            df.to_csv('out.csv', index=False)
            print(f"Processing file {file}")
        
        with open(str(i) + 'r/' + file, 'r') as f:
            text = f.readlines()[1]
            text = text.split(", ")
            textSet = set(text)
            #print(textSet)
            
            for word in textSet:
                value = binary_search_pandas(df, word)
                
                if value == -1:
                    if word == "nan":
                        value = 289510 
                    if word == "null":
                        value = 302142
                    else: 
                        print("damn")
                        nowords.append(word)
                    continue
                
                old_val = df.loc[value, 'g' + str(i)]
                #df.loc[value, 'g1'] = dict[word] + old_val
                df.loc[value, 'g' + str(i)] = old_val + 1
                #df.loc[df['words'] == word, 'g1'] = dict[word]
                    #print("found")
                    
    df.to_csv('out.csv', index=False)

df.to_csv('out.csv', index=False)

# write nowrods to file
with open('nowords.txt', 'w') as f:
    f.write('\n'.join(nowords))
                    

    


# for file in files[:2]:
#     print(f"Processing file {file}")
#     with open('freqs/' + file, 'r') as f:
#         text = f.read()
        
#         text = text.split(", ")
#         #print(text)
        
#         for word in text:
#             dict = {word.split(": ")[0]: int(word.split(": ")[1]) for word in text}
#         #text = {word.split(": ")[0]: int(word.split(": ")[1]) for word in text}
#         #print(dict)
#         #input()
        
#         for word in dict:
#             #print(word)
#             value = binary_search_pandas(df, word)
#             if value == -1:
#                 print("damn")
#                 continue
            
#             old_val = df.loc[value, 'g1']
#             #df.loc[value, 'g1'] = dict[word] + old_val
#             df.loc[value, 'g1'] = old_val + 1
#             #df.loc[df['words'] == word, 'g1'] = dict[word]
#                 #print("found")
        
#         #save to csv
#         df.to_csv('out.csv', index=False)