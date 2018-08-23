import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''
    def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"James")
    self.assertEqual(self.new_user.last_name,"Muriuki")
    self.assertEqual(self.new_user.email,"asumanibrighton@gmail.com")
    self.assertEqual(self.new_user.username,"asu")
    self.assertEqual(self.new_user.password,"newa$um0ney")
    self.assertEqual(self.new_user.confirmpassword,"newa$um0ney")



if __name__ == '__main__':
    unittest.main()
