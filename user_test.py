import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Brighton","Asumani","bright@gmail.com","asu","password","password") # create user object


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

    def test_save_user(self):
        '''
        saving users details
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","test@gmail.com","tested","pass","pass") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    # other test cases here
    def test_save_multiple_users(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","test@gmail.com","tested","pass","pass") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)



if __name__ == '__main__':
    unittest.main()
