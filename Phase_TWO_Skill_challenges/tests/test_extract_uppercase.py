from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_with_one_uppercase_and_one_lowercase():
    result = extract_uppercase("hello WORLD") 
    assert result == ["WORLD"]

# """
# Given two uppercase words
# It returns a list with both words
# """
def tests_two_uppercase():
    assert extract_uppercase("HELLO WORLD") == ["HELLO", "WORLD"]

# """
# Given two lowercase words
# It returns an empty list
# """
def test_with_only_lowercase_words():
    assert extract_uppercase("hello world") == []

# """
# Given a lower and a mixed case word
# It returns an empty list
# """
def test_mixed_case_and_lowercase():
    result = extract_uppercase("hello WoRLD YES")
    assert result == ["YES"]

# """
# Given a lowercase word and an uppercase word with an exclamation mark
# It returns a list with the uppercase word, no exclamation mark
# """
def test_a_mix_of_upper_and_lower():
    result = extract_uppercase("hello WORLD!")
    assert result == ["WORLD"]

"""
Given an empty string
It returns an empty list
"""

def test_extract_uppercase():
    result = extract_uppercase("")
    assert result == []

"""
Given a None value
It throws an error
# """
# extract_uppercase(None) throws an error