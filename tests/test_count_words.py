from lib.count_words import *

def test_returns_1():
    result = count_words("Hello")
    assert result == 1

def test_returns_multiwords():
    result = count_words("Hello world")
    assert result == 2

def test_returns_zero():
    result = count_words("")
    assert result == 0

def test_with_punctuation():
    result = count_words("I like python!")
    assert result == 3

def test_only_punctuation():
    result = count_words("! , ) / , ")
    assert result == 0




