#!/usr/local/bin/python3
'''
LPTHW exercise 25
Even More Practice
'''

def break_words(stuff):
    '''break up words'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''sorts the words'''
    return sorted(words)

def print_first_word(words):
    '''prints first word after popping it'''
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    '''prints last word after popping it'''
    word = words.pop(-1)
    print(word)

def sort_sentance(sentance):
    '''takes in a full sentance and returns sorted words'''
    words = break_words(sentance)
    return sort_words(words)

def print_first_and_last(sentance):
    '''prints the first and last words'''
    words = break_words(sentance)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentance):
    '''sorts the words then prints first and last one'''
    words = sort_sentance(sentance)
    print_first_word(words)
    print_last_word(words)
