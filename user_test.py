import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Brighton","Asumani","bright@gmail.com","asu","password","password") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Brighton")
        self.assertEqual(self.new_user.last_name,"Asumani")
        self.assertEqual(self.new_user.email,"bright@gmail.com")
        self.assertEqual(self.new_user.username,"asu")
        self.assertEqual(self.new_user.password,"password")
        self.assertEqual(self.new_user.confirmpassword,"password")


if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    unittest.main()
