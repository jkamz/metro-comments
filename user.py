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
from models import UserModel,users
import datetime


class User:
    def __init__(self):
        self.logged_in = False
        self.last_logged_in_at = None

    def signUp(self):

        username = input("please enter your username:")
        email = input("please enter your email:")
        password = input("please enter your password:")
        role = input("enter role:")

        UserModel().signup(username, email, password, role)


    def signin(self):
        username = input("Enter Username:")
        password = input("Enter Password")

        user = [user for user in users if user["username"]==username and user["password"]==password]

        if user:
            self.logged_in = True
            self.last_logged_in_at = datetime.datetime.now().date()
            print(f"{username} signed in")
            return self.logged_in
            
class Moderator(User):
    pass


class Admin(Moderator):
    pass
