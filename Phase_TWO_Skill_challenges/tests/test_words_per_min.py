from lib.words_per_min import *
import pytest

"""
Given 200 words
It returns a reading time of 1 
"""

def test_200_words():
    text = " ".join(["word" for i in range(0,200)])
    result = reading_time(text)
    assert result == 1.0

"""
Given 400 words
It returns a reading time of 1 
"""

def test_400_words():
    text = " ".join(["word" for i in range(0,400)])
    result = reading_time(text)
    assert result == 2.0

    """
Given 100 words
It returns reading time of 0.5
"""
def test_100_words():
    text = " ".join(["word" for i in range(0,100)])
    result = reading_time(text)
    assert result == 0.5

"""
given an empty string
it returns an error
"""
def test_no_words():
    with pytest.raises(Exception) as e:
        reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for empty text."
