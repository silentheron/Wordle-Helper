# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:28:26 2022

@author: boris
@function: Looks for possible words matching the clues given
"""
import re
import random


def contains_all(str,set):
    return 0 not in [c in str for c in set]

def contains_none(str,set):
    return 0 in [c in str for c in set]

def possible_matches(choice,unwanted_letters):
    
    if choice == '1':
        user_input = input("Enter the letters you guess correctly with dots inbetween them: ").upper()
        for letter in user_input:
            if ord(letter) < 100 or ord(letter) > 132 or not '.' or len(user_input) > 5 or len(user_input) < 5:
                print('Invalid String')
                break
        pattern = f'^{user_input}$'
        print("Matching words: ")
        for word in words:
            if re.match(pattern, word):
                print(word)
    
    elif choice == '2':
        user_input = list(input("Enter the letters you guess correctly with no spaces between them: ").upper())
        print("Matching words: ")
        for word in words:
            if contains_all(word, user_input) and contains_none(word, unwanted_letters):
                print(word)
    
    elif choice == '3':
        user_input = input("Enter the pattern followed by a space follower by letters: ").upper().split(' ')
        pattern = f'^{user_input[0]}$'
        guessed_letters = list(user_input[1])
        print("Matching words: ")
        for word in words:
            if re.match(pattern, word):
                if contains_all(word, guessed_letters):
                    if contains_none(word, unwanted_letters):
                        print(word)


words = open("five_letter_words.txt").read().split('\n')

unwanted_letters = input("Write down letters you tried and did not match")
user = input("""1. For correctly places Letters
             2. Only for correctly Guessed Letters
             3. If you have both\n""")
             
possible_matches(user, unwanted_letters)


        
