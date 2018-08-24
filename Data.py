import pyperclip

class User:
        #Class that generates new instances of users

        user_list = [] # Empty user list
        def __init__(self,first_name,last_name,user_name,email,password):

          # docstring removed for simplicity

            self.first_name = first_name
            self.last_name = last_name
            self.username = user_name
            self.email = email
            self.password = password

        def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            User.user_list.append(self)



class Credential:

    credential_list = []
    #Class that generates new instances of users
    def __init__(self,account,password,secretkey):

      # docstring removed for simplicity

        self.account = account
        self.password = password
        self.secretkey = secretkey

    def save_credential(self):

        '''
        save_user method saves user objects into user_list
        '''

        Credential.credential_list.append(self)


    def delete_credential(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        Credential.credential_list.remove(self)


    @classmethod
    def find_by_secretkey(cls,secretkey):
        '''
        Method that takes in a number and returns a contact that matches that secretkey.

        Args:
            secretkey to search for
        Returns :
            credential of person that matches the secretkey.
        '''

        for credential in cls.credential_list:
            if credential.secretkey == secretkey:
                return credential


    @classmethod
    def credential_exist(cls,secretkey):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.credential_list:
            if account.secretkey == secretkey:
                    return True

        return False
