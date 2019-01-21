from models import UserModel
from validators import UserValidation

validate = UserValidation()

class User:

    def signUp(self):

        username = input("please enter your username:")
        email = input("please enter your email:")
        em = validate.validate_email(email)
        if not em:
            return "You have entered wrong email"
        password = input("please enter your password:")
        pas = validate.validate_password(password)
        if pas:
            UserModel().signup(username, email, password, role)
        else:
            return "Password is invalid"
        role = input("enter role:")


class Moderator(User):
    pass


class Admin(Moderator):
    pass