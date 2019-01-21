""" The metro-comment app is tested here """
import unittest
from user import User


class BaseTest(unittest.TestCase):
    def __init__(self):
        self.sample_user = {
            "username": "TitoG",
            "email": "titog@eg.com",
            "password": "pass123"
        }


class TestUser(BaseTest):

    def test_user_signup(self):
        response = User.save(self.sample_user)

        self.assertEqual(response.get("username"), "TitoG")
        self.assertEqual(response.get("password"), "pass123")

if __name__ == '__main__':
    unittest.main()
