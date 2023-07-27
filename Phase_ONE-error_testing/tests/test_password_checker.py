import pytest
from lib.password_checker import *

def test_check_password_works():
    password = PasswordChecker()
    assert password.check("Password") == True

def test_password_is_short():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."







# class PasswordChecker:
#     def check(self, password):
#         if len(password) >= 8:
#             return True
#         else:
#             raise Exception("Invalid password, must be 8+ characters.")