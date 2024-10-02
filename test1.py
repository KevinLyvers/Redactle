# alphabatize all words in words.txt

with open('words.txt', 'r') as f:
    words = f.read().split(", ")
    words = [word.lower() for word in words]
    words.sort()
    
# write to wordsAlpha.txt

print(len(words))

wordsStr = ", ".join(words)
with open('wordsAlpha.txt', 'w') as f:
    f.write(wordsStr)