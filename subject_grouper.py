# takes in all the text files from a subject and finds the percent of each word use

num = 5

# read all text files in folder 6
import os

arr = os.listdir(str(num))

master_list = {} # dictionary to hold the frequency of each word

for i, file in enumerate(arr):
    print(f"Processing file {i}")
    with open(str(num) + '/' + file, 'r') as f:
        text = f.read()[1:]
        words = text.split(", ")
        
        # lowercase all the words
        words = [word.lower().strip() for word in words]
        
        # get rid of duplicates 
        words = list(set(words))
        
        
        for word in words:
            if word in master_list:
                master_list[word] += 1
            else:
                master_list[word] = 1
        
# check against words.txt if word is valid
with open('words.txt', 'r') as f:
    #continue
    valid_words = f.read().split()
    valid_words = [word.lower() for word in valid_words]
    
    for word in list(master_list.keys()):
        # Binary search to check if word is valid
        left = 0
        right = len(valid_words) - 1
        while left <= right:
            #print(f"left: {valid_words[left]}, right: {valid_words[right]}")
            mid = (left + right) // 2
            if valid_words[mid] == word:
                break
            elif valid_words[mid] < word:
                left = mid + 1
            else:
                right = mid - 1
        else:
            #print(f"left: {valid_words[left]}, right: {valid_words[right]}")
            #print(f"left number: {left}, right number: {right}")
            print(f"Removing {word}")
            del master_list[word]
    
    # since valid_words are in alphabetical order, we can use binary search 
    
# sort master list by value
master_list = dict(sorted(master_list.items(), key=lambda x: x[1], reverse=True))

for word, freq in master_list.items():
    percentage = (freq / len(arr))
    master_list[word] = percentage

# write the master list to a file
with open('master_list' + str(num) + '.txt', 'w') as f:
    for word, freq in master_list.items():
        f.write(f"{word}: {freq}\n")