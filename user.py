from models import UserModel


class User:

    def signUp(self):

        username = input("please enter your username:")
        email = input("please enter your email:")
        password = input("please enter your password:")
        role = input("enter role:")

        UserModel().signup(username, email, password, role)


class Moderator(User):
    pass


class Admin(Moderator):
    pass
