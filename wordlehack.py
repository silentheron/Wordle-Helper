# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:59:09 2022

@author: boris
"""

import requests
from bs4 import BeautifulSoup

# # get the page 
# page = requests.get("https://www.bestwordlist.com/5letterwords.htm")
# # all the words are contained in 'span' elements inside the html
# soup = BeautifulSoup(page.content, 'html.parser')
# spans = soup.find_all('span')



# makes a list of words and appends them to the text file
def scrape_words(spans, file):
    words_soup = []
    for i in range(len(spans)):
        words_soup.append(spans[i].get_text())
    words_rough = words_soup[1:-3]
    
    # adds each word seperataley to a .txt file
    for word in words_rough:
        clean_words = word.strip().split(' ')
        for word in clean_words:
            file.write(word + '\n')


text_file = open('five_letter_words.txt', 'w')


status_code = True
page_counter = 1
while(status_code):
    if(page_counter == 1):
        page = requests.get("https://www.bestwordlist.com/5letterwords.htm")
        status_code = False if str(page.status_code)[0] != '2' else True
        soup = BeautifulSoup(page.content, 'html.parser')
        spans = soup.find_all('span')
    else:
        page = requests.get(f'https://www.bestwordlist.com/5letterwordspage{page_counter}.htm')
        status_code = False if str(page.status_code)[0] != '2' else True
        print(status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        spans = soup.find_all('span')
    
    scrape_words(spans, text_file)
    page_counter += 1
    
    
    
    
text_file.close()
    
    
    
    
    
    
    
    