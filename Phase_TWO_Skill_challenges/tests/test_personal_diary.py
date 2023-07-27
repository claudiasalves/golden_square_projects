from lib.personal_diary import *



def test_returns_words_if_5():
    result = make_snippet("Hello how are you today?")
    assert result == "Hello how are you today?"

def test_returns_words_and_if_more_than_5():
    result = make_snippet("Hello my name is Claudia and yours?")
    assert result == "Hello my name is Claudia..."


def test_returns_empty_string():
    result = make_snippet("")
    assert result == ""