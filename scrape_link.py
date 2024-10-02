### webscrape links from a given url

import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

# URL of the Wikipedia page you want to scrape
urls = ["https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/People","https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/History", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Geography", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Arts", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Philosophy_and_religion", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Everyday_life", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Society_and_social_sciences", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Biology_and_health_sciences", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Physical_sciences", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Technology", "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Mathematics"]
urls = ["https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/4/Mathematics"]

master_list = []

idx = 0
for url in urls:
    total_text = ""
    idx += 1

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the first paragraph (usually in a <p> tag)
        test = soup.find_all('a')

        for i in range(0, len(test)):
            try:
                ###print(test[i])
                url = test[i].get('href')
                if not "." in url:
                    if not "//" in url:
                        if not ":" in url:
                            if not "#" in url:
                                if not "Main_Page" in url:
                                    ###print("url:      ",url)
                                    ##master_list.append(test[i].get('href')+"} "+str(idx)) 
                                    master_list.append(test[i].get('href').split("/")[-1]) 
                                    ###break
                ###urlNot.append(test[i].get('href'))
                                    
            except:
                continue
            ##total_text = total_text + test[i].text.lower()
        
    ##s = re.sub(r'\W+', ' ', total_text)
    ##print(s)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
print(master_list)
set(master_list)

###write a list to a file
with open('linksMATH.txt', 'w') as f:
    for item in master_list:
        f.write("%s\n" % item)
        
print("done")