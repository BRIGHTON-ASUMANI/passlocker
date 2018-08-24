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
    



class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("twitter", "password", 'secretkey') # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.password,"password")
        self.assertEqual(self.new_credential.secretkey,"secretkey")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","password",'secretkey') # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

# other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","password",'seccretkey') # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Twitter","password",'secretkey') # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)
    def test_find_credential_by_secretkey(self):
        '''
        test to check if we can find a credential by secretkey and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("twitter",'password','secretkey') # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_secretkey("secretkey")

        self.assertEqual(found_credential.secretkey,test_credential.secretkey)


    def test_crendential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","secretkey") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("secretkey")

        self.assertTrue(credential_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)






if __name__ == '__main__':
    unittest.main()
