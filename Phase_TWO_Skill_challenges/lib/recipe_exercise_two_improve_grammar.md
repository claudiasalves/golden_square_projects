# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

We'll ignore any intermediate sentences.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def correct_grammar(text):
    """estimates reading time for a text, considering 200 words per minute 


    Parameters: (list all parameters and their types)
        text: a string containing words and punctuation (e.g. "hello world")

    Returns: (state the return value and its type)
        Boolean: returns true if text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, and false otherwise

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence that starts with a capital letter and ends with . ? !  
It returns True
"""
correct_grammar("How are you?") => True

"""
Given a sentence that does not start with capital letter nor ends with . ? !
It returns False
"""
correct_grammar("how are you") => False

"""
Given a sentence that does start with capital letter but not ends with . ? !
It returns False
"""
correct_grammar("How are you") => False

"""
Given a sentence that does not start with capital letter but ends with . ? !
It returns False
"""
correct_grammar("how are you?") => False

"""
Given an empty string
It returns an error
"""
correct_grammar("") => "There is no text to analyse."


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


