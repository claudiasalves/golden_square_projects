# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_todo(text):
    """estimates reading time for a text, considering 200 words per minute 


    Parameters: (list all parameters and their types)
        text: a string containing words  (e.g. "hello world")

    Returns: (state the return value and its type)
        Boolean: returns "Don't forget this" if text includes #TODO, and "All done!" otherwise

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
Given text that includes #TODO in the beginning
It returns "Don't forget this"
"""
check_todo("#TODO walk the dog") => "Don't forget this"

"""
Given text that includes #TODO in the end
It returns "Don't forget this"
"""
check_todo(" walk the dog #TODO") => "Don't forget this"

"""
Given text does not includes #TODO 
It returns "All done!"
"""
check_todo("Walk the dog") => "All done!"

"""
Given text includes TODO without #
It returns "All done!"
"""
check_todo("Walk the dog TODO") => "All done!"

"""
Given text includes # without TODO
It returns "All done!"
"""
check_todo("Walk the dog #") => "All done!"

"""
Given an empty string
It returns an error
"""
check_todo("") => "There are no tasks."


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


