# count how many files in each folder

import os

all_words = ""

for i in range(1,12):
    print(f"Processing folder {i}")
    arr = os.listdir(str(i) + 'r')
    for file in arr:
        with open(str(i) + 'r/' + file, 'r') as f:
            text = f.readlines()[1]
            all_words += text

all_words = all_words.split(", ")
all_words = list(set(all_words))

print(len(all_words))

# turn list to string
words = ', '.join(all_words)

#write to words.txt
with open('words.txt', 'w') as f:
    f.write(words)
    