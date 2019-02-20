import unittest
from app.models import User
from app import db

#the setup method creates an instances of our user
class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Francis',password = 'Password', email = 'fkaragu@gmail.com')

    def save_user(self):
        db.session.add(self.new_user)
        db.session.commit()

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Password'))
