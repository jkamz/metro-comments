import re
from models import users,comments
from models import UserModel

usrs = UserModel()


class UserValidation():
    def __init__(self):
        self.users = users
        self.comments = comments

    def validate_password(self, password):
        """Check if the password is valid.

            This function checks the following conditions
            if its length is greater than 6 and less than 8
            if it has at least one uppercase letter
            if it has at least one lowercase letter
            if it has at least one numeral
            if it has any of the required special symbols
            """
        SpecialSym=['$','@','#']
        return_val=True
        if len(password) < 6:
            return_val=False
        if len(password) > 8:
            return_val=False
        if not any(char.isdigit() for char in password):
            return_val=False
        if not any(char.isupper() for char in password):
            return_val=False
        if not any(char.islower() for char in password):
            return_val=False
        if not any(char in SpecialSym for char in password):
            return_val=False
        if return_val:
            print('Ok')
        return return_val

    def validate_email(self, email):
        """Method to check entry of invalid password """
        exp = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(exp, email)