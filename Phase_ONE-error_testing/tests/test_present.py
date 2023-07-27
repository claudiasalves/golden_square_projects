import pytest
from lib.present import *


def test_wrapping_and_unwrapping():
    present = Present()
    present.wrap("bycicle")
    assert present.unwrap() == 'bycicle'

def test_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_contents_already_wrapped():
    present = Present()
    present.wrap("bycicle")
    with pytest.raises(Exception) as e:
        present.wrap("baloon")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_not_wrapping_twice():
    present = Present()
    present.wrap("bycicle")
    with pytest.raises(Exception) as e:
        present.wrap("baloon")
    assert present.unwrap() == 'bycicle'




# class Present:
#     def __init__(self):
#         self.contents = None

#     def wrap(self, contents):
#         if self.contents is not None:
#             raise Exception("A contents has already been wrapped.")
#         self.contents = contents

#     def unwrap(self):
#         if self.contents is None:
#             raise Exception("No contents have been wrapped.")
#         return self.contents