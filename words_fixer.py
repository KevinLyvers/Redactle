# why is words.txt not in alphabetical order!!!

# alphabetize words.txt and put everything in lowercase

with open('words.txt', 'r') as f:
    words = f.read().split()
    words = [word.lower() for word in words]
    words.sort()
    
with open('words.txt', 'w') as f:
    for word in words:
        f.write(f"{word}\n")