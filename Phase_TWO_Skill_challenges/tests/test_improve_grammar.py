from lib.improve_grammar import *
import pytest
"""
Given a sentence that starts with a capital letter and ends with . ? !  
It returns True
"""
def test_capital_letter_and_correct_ending():
    result = improve_grammar("How are you?") 
    assert result == True

"""
Given a sentence that does not start with capital letter nor ends with . ? !
It returns False
"""
def test_no_capital_letter_nor_correct_ending():
    result = improve_grammar("how are you+") 
    assert result == False

"""
Given a sentence that does start with capital letter but not ends with . ? !
It returns False
"""
def test_capital_letter_but_no_correct_ending():
    result = improve_grammar("How are you+") 
    assert result == False

"""
Given a sentence that does not start with capital letter but ends with . ? !
It returns False
"""
def test_no_capital_letter_but_correct_ending():
    result = improve_grammar("how are you?") 
    assert result == False

"""
Given an empty string
It returns an error
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        improve_grammar("")
    error_message = str(e.value)
    assert error_message == "There is no text to analyse."