from my_grep.searching.pattern_searching import regex_pattern_search
from my_grep.searching.pattern_searching import word_matching

import pytest

def test_regex_pattern_search():
    assert regex_pattern_search(r'[A-Za-z0-9._%+-]+@gmail\.com', 'user@gmail.com', False)

def test_regex_false():
    assert regex_pattern_search(r'[A-Za-z0-9._%+-]+@gmail\.com', 'eu sunt', False) == False

def test_regex_case_insensitive():
    assert regex_pattern_search(r'[A-Za-z0-9._%+-]+@gmail\.com', 'User@gmail.com', True)

def test_word_matching():
    assert word_matching('eu', False, False, 'eu sunt')
    
def test_word_matching_false():
    assert word_matching('eu', False, False, 'e sunt') == False

def test_word_matching_case_insensitive():
    assert word_matching('EU', True, False, 'eu sunt')

def test_word_matching_regex():
    assert word_matching(r'[A-Za-z0-9._%+-]+@gmail\.com', False, True, 'user@gmail.com')

def test_word_matching_regex_insensitive():
    assert word_matching(r'[A-Za-z0-9._%+-]+@gmail\.com', True, True, 'USER@gmail.com')

def test_word_matching_regex_false():
    assert word_matching(r'[A-Za-z0-9._%+-]+@gmail\.com', False, False, 'eu sunt') == False






# def word_matching(word,i,e, line):
#     match_found  = False
#     if e: 
#         match_found = regex_pattern_search(word, line, i)
#     else:                
#         if i:
#             if word.lower() in line.lower():
#                 match_found = True            
#         else:
#             if word in line :
#                 match_found = True
#     return match_found