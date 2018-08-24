import pyperclip
import unittest # Importing the unittest module
from Data import User,Credential # Importing the user class

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Brighton","Asumani","bright@gmail.com","asu","password") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Brighton")
        self.assertEqual(self.new_user.last_name,"Asumani")
        self.assertEqual(self.new_user.email,"asu")
        self.assertEqual(self.new_user.username,"bright@gmail.com")
        self.assertEqual(self.new_user.password,"password")

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
            test_user = User("Test","user","test@gmail.com","tested","pass") # new user
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
            test_user = User("Test","user","test@gmail.com","tested","pass") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    # # More tests above
    # def test_delete_user(self):
    #         '''
    #         test_delete_user to test if we can remove a user from our user list
    #         '''
    #         self.new_user.save_user()
    #         test_user = User("Test","user","test@gmail.com","tested","pass","pass") # new user
    #         test_user.save_user()
    #
    #         self.new_user.delete_user()# Deleting a user object
    #         self.assertEqual(len(User.user_list),1)
    #
class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("twitter", "password") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.password,"password")

    # def test_find_user_by_number(self):
    #     '''
    #     test to check if we can find a user by phone number and display information
    #     '''
    #
    #     self.new_user.save_user()
    #     test_user = User("Test","user","test@gmail.com","tested","pass","pass") # new user
    #     test_user.save_user()
    #
    #     found_user = User.find_by_email("test@gmail.com")
    #
    #     self.assertEqual(found_user.email,test_user.email)
    #
    #
    # def test_user_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the user.
    #     '''
    #
    #     self.new_user.save_user()
    #     test_user = User("Test","user","test@gmail.com","tested","pass","pass") # new user
    #     test_user.save_user()
    #
    #     user_exists = User.user_exist("test@gmail.com")
    #
    #     self.assertTrue(user_exists)
    #
    #
    # def test_display_all_users(self):
    #     '''
    #     method that returns a list of all users saved
    #     '''
    #
    #     self.assertEqual(User.display_users(),User.user_list)
    #
    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found user
    #     '''
    #
    #     self.new_user.save_user()
    #     User.copy_email("test@gmsil.com")
    #
    #     self.assertEqual(self.new_user.email,pyperclip.paste())
    #


if __name__ == '__main__':
    unittest.main()
