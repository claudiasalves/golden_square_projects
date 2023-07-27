# from lib.challenge_check_todo import *
# import pytest 

# """
# Given text that includes "#TODO" in the beginning
# It returns "Don't forget this"
# """
# def test_check_todo_with_hashtag_beginning():
#     result = check_todo("#TODO walk the dog") 
#     assert result == "Don't forget this"

# """
# Given text that includes #TODO in the end
# It returns "Don't forget this"
# """
# def test_check_todo_with_hashtag_at_end():
#     result = check_todo(" walk the dog #TODO")
#     assert result == "Don't forget this"

# """
# Given text does not includes #TODO 
# It returns "All done!"
# """

# def test_check_no_todo():
#     result = check_todo("Walk the dog")
#     assert result == "All done!"

# """
# Given text includes TODO without #
# It returns "All done!"
# """
# def test_todo_with_no_hashtag():
#     result = check_todo("Walk the dog TODO")
#     assert result == "All done!"

# """
# Given text includes # without TODO
# It returns "All done!"
# """
# def test_hasthag_with_no_todo():
#     result = check_todo("Walk the dog #") 
#     assert result == "All done!"

# """
# Given an empty string
# It returns an error
# """
# def test_no_text():
#     with pytest.raises(Exception) as e:
#         check_todo("")
#     error_message = str(e.value)
#     assert error_message == "There are no tasks."