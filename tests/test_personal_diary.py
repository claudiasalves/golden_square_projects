from lib.personal_diary import *

def test_make_snippet():
    result = make_snippet("Hello")
    assert result == "Hello"

def test_return_first_five_words():
    result = make_snippet("Hello everyone my name is")
    assert result == "Hello everyone my name is"

def test_return_first_five_words_plus_dots():
     result = make_snippet ("Hello everyone my name is Claudia")
     assert result == "Hello everyone my name is..."
