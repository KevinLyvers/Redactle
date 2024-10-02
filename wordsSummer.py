# 9/13
# add up how many times words appear in each text file
# and writes to files in freqs folder

import os

# get all files from folder 1r
arr = os.listdir('1r')
import time
start = time.time()

for i, file in enumerate(arr[190:]):
    if i % 25 == 0:
        print(f"Processing file {i}")
        print(f"Time elapsed: {time.time() - start}")
    with open('1r/' + file, 'r') as f:
        text = f.readlines()
        name = text[0]
        text = text[1]
        # put in fomrat word:freq
        text = text.split(", ")
        #print(text)

        # get frequency of each word
        text = {word: text.count(word) for word in text}
        
        text = sorted(text.items(), key=lambda x: x[1], reverse=True)
        
        #text = {word[0]: int(word[1]) for word in text}
        
        #print(text)
        
        text_str = ", ".join([f"{word[0]}: {word[1]}" for word in text])

        # write freqs to file 
        with open('freqs/' + name.split("/")[-1][:-1] + ".txt", 'w') as f:
            f.write(text_str)
            
        