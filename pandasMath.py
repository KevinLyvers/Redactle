#read in the outMath.csv
import pandas as pd
import time

time0 = time.time()

types = {'words': str, 'g1': float, 'g2': float, 'g3': float, 'g4': float, 'g5': float, 'g6': float, 'g7': float, 'g8': float, 'g9': float, 'g10': float, 'g11': float, 'gmath1': float, 'gmath2': float, 'gmath3': float, 'gmath4': float, 'gmath5': float, 'gmath6': float, 'gmath7': float, 'gmath8': float, 'gmath9': float, 'gmath10': float, 'gmath11': float}
totals = [1923,688,1196,662,431,473,928,1481,1102,741,300]
total = sum(totals)
df = pd.read_csv('outProb.csv' , dtype=types)

# set to inverse 
# for every word
for word in range(len(df)):
#for word in range(425726, 425928):
    if word % 10000 == 0:
        print(f"Processing word {df.iloc[word, 0]}")
        print(f"Time elapsed: {time.time() - time0}")
        print(f"Time remaining: {(time.time() - time0) / (word + 1) * (len(df) - word) / 60}")
    for j in range(1, 12):
        sum = 1.0
        for k in range(1, 12):
            if j != k:
                sum *= df.iloc[word, k]
            else:
                sum *= (1 - df.iloc[word, k])
                
        # put data in gmath 
        df.iloc[word, 11 + j] = sum
    #df[f'gmath{i}'] = sum
    
    #total = sum(df.iloc[i, 1:])
    
    
# save to csv
df.to_csv('outConfirmInv.csv', index=False)