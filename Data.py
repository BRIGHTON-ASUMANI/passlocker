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
    def __init__(self,account,password,):

      # docstring removed for simplicity

        self.account = account
        self.password = password

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
    def find_by_account(cls,account):
        '''
        Method that takes in an account and returns an account that matches the name.

        Args:
            number: account to search for
        Returns :
            User of person that matches the email.
        '''

        for user in cls.credential_list:
            if credential.account == account:
                return account

    @classmethod
    def credential_exist(cls,password):
        '''
        Method that checks if an account exists from the credential list .
        Args:
            account: account to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for account in cls.credential_list:
            if credential.account == account:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,email):
        user_found = User.find_by_email(email)
        pyperclip.copy(user_found.email)
