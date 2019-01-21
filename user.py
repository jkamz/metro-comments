from models import UserModel


class User:

    def signUp(self):

        username = input("please enter your username")
        email = input("please enter your email")
        password = input("please enter your password")
        confirm_password = input("please confirm password")
        role = input("enter role")

        UserModel.signup(username, email, password, confirm_password, role)


class Moderator(User):
    pass


class Admin(Moderator):
    pass
