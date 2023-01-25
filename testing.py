import unittest
from backend import *


class testCode(unittest.TestCase):
    """
        a class that is used to test all the commands performed by the
        client server system
    """
    def test_login(self):
        '''
            test for login operation
        '''
        result = login("phani","123")
        self.assertEqual(result,"logged in")
        result = login("rob","567")
        self.assertEqual(result,"username or password mismatch")
        result = login("phani","123")
        self.assertEqual(result,"user already logged in")


    def test_register_user(self):
        '''
            test for registering user
        '''
        result = register("roger","123")
        self.assertEqual(result,"user created")
        result = register("roger","123")
        self.assertEqual(result,"user with same name exists")

    def test_logout(self):
        '''
            test for logging out user
        '''
        result = logout("phani")
        self.assertEqual(result,"user logged out")

    def test_create_folder(self):
        '''
            test for creating folder
        '''
        obj = User("phani")
        result = obj.create_directory("news")
        self.assertEqual(result,"created !!!")
        result = obj.create_directory("news")
        self.assertEqual(result,"cannot create the folder as it already exists")


if __name__ =='__main__':
    unittest.main()
