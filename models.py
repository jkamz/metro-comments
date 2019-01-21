""" All the data will be stored here """

users = []

comments = []


class UserModel():
    """
    user model
    """

    def signup(self, username, email, password, role):
        """
        user signup model
        """

        user = {
            "id": len(users) + 1,
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }

        users.append(user)
        return user
