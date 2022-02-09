# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:32:24 2022

@author: boris
"""

import re
wordlist = open('five_letter_words.txt', 'r').read().split('\n')


pattern = '^S.I.L$'
word1 = 'titty'.upper()
for word in wordlist:
    if re.match(pattern, word):
        print(word)
        
