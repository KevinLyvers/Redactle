# this takes all the urls from links.txt and webscrapes the text and puts them in 
# text files in a CSV format of all lowercase words in order (so just a copy of all articles)

# writes to r folders for raw text

# checked: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# raw checked: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11

num = -1

# read from links.txt 
with open('links.txt') as f:
    links = f.readlines()
    
good_links = []
for link in links:
    #print(link)
    if "} " + str(num) + "\n" in link:
        good_links.append(link)
        
# webscape the links from the good_links list

import requests
import re
from bs4 import BeautifulSoup

print(len(good_links))

for i, link in enumerate(good_links):
    print(f"Processing link {i}")
    url = ('https://en.wikipedia.org' + link.split("}")[0]).strip()
    print(f"Retrieving page from {'url'}")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # get main body text of the article
        body = soup.find('div', class_='mw-body-content')
        
        main_body = body.find_all('p')
        
        # only things in paragraph
        
        for j, p in enumerate(main_body):
            main_body[j] = p.get_text(separator=' ')
        
        
        # get just the text with spaces between paragraphs
        #text = main_body.get_text(separator=' ')
        
        text_str = ' '.join(main_body)
        
        # get rid of all things between square brackets
        text = re.sub(r'\[.*?\]', ' ', text_str)
        
        # get rid of all special characters 
        text = re.sub(r'[^A-Za-z0-9 ]', ' ', text)
        
        # text to lowercase
        text = text.lower()
        
        text_array = text.split()
        
        text = ', '.join(text_array)
        
        

        
        
        
        
        # remove all the tags 
        #text = re.sub(r'<[^>]*>', ' ', str(main_body))
                
        #print(text)
        
        
        # remove any special characters
        #text = re.sub(r'[^A-Za-z0-9 ]', ' ', text)
        
        # get a set of all the words
        #words = set(text.split())
        
        
        # convert set to string
        
        
        # print(len(words))
        # if len(words) == 0:
        #     print(url)
        
        #     input()
        
        
        
        # get a frequency count of the words
        # word_freq = {}
        # for word in text.split():
        #     if word in word_freq:
        #         word_freq[word] += 1
        #     else:
        #         word_freq[word] = 1
        # # sort the dictionary by value
        # word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
        
        # print(word_freq)
        
        # # dict to string
        # word_freq_str = ""
        # for word, freq in word_freq.items():
        #     word_freq_str += f"{word}: {freq}\n"
            
        # write the word frequency to a file
        with open(str(num) + 'r/'+ str(i) +'.txt', 'w') as f:
            f.write(url + '\n')
            f.write(text)
            
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")