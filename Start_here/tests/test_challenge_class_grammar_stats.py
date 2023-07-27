from lib.challenge_class_grammar_stats import *
"""
if given a word that start with capital letter and ends with a sentence-ending punctuating mark
returns True
"""

def test_sentence_is_correct():
    sentence = GrammarStats()
    result = sentence.check("Hello world!")
    assert result == True

"""
if word start with capitall letter but does not end with sentence-ending punctuation
return False
"""
def test_sentence_does_not_finish_with_correct_punctuation():
    sentence = GrammarStats()
    result = sentence.check("Hello world")
    assert result == False

"""
if word does not start with capital letter but finishes with correct punctuation
return False
"""

def test_sentence_does_not_start_with_capital_letter():
    sentence = GrammarStats()
    result = sentence.check("hello world.")
    assert result == False

"""
if 4 texts have been checked and only 2 passed
returns 50
"""

# def test_sentence_does_not_start_with_capital_letter():
#     sentence = GrammarStats()
#     result = sentence.percentage_good("hello world.")
#     assert result == False