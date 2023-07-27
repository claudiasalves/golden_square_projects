# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text):
    """estimates reading time for a text, considering 200 words per minute 


    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "hello world")

    Returns: (state the return value and its type)
        float: a number that represents time 

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
Given 200 words
It returns a reading time of 1 
"""
reading_time(word*200) => 1.0

"""
Given 400 words
It returns reading time of 2.0
"""
reading_time(word*400) => 2.0

"""
Given 100 words
It returns reading time of 2.0
"""
reading_time(word*100) => 0.5

"""
given an empty string
it returns an error
"""
reading_time("") => "Can't estimate reading time for an empty text."


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


