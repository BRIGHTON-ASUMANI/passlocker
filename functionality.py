#!/usr/bin/env python3.6
from Data import User, Credential

def create_user(first_name,last_name,user_name,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,user_name,email,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def create_credential(account,password,secretkey):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,password,secretkey)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(secretkey):
    '''
    Function that finds a credential by secretkey and returns the credential
    '''
    return Credential.find_by_secretkey(secretkey)

def check_existing_credentials(secretkey):
    '''
    Function that check if a credential exists with that secretkey and return a Boolean
    '''
    return Credential.credential_exist(secretkey)

def display_secretkeys():
    '''
    Function that returns all the saved secretkeys
    '''
    return Credential.display_secretkeys()

def main():
    # user_list = []
    # # users = {}
    # status = ""
    # def displayMenu():
    #     status = input("welcome to the master password please sign up by pressing s to or  login by pressing l \n" )
    #     print("-"*40)
    #     if status == "l":
    #         oldUser()
    #     elif status == "s":
    #         newUser()
    #     else:
    #             print('incorrect input please try again')
    #
    # def newUser():
    #     f_name = input("firstname \n")
    #     print("-"*40)
    #
    #     l_name = input("lastname \n")
    #     print("-"*40)
    #
    #     u_name = input("username \n")
    #     print("-"*40)
    #
    #     email = input("email \n")
    #     print("-"*40)
    #
    #     if u_name in users:
    #         print("\n username already\n")
    #         print("\n")
    #     else:
    #         p_name = input("password\n")
    #         print("-"*40)
    #         users[u_name] = p_name
    #         print("\n User registered\n")
    #
    # def oldUser():
    #     u_name = input ("enter username\n")
    #     print("-"*40)
    #     p_name = input ("enter password\n")
    #     print("-"*40)
    #
    #     if u_name in users and users[u_name] == p_name:
    #         print("\nyou are logged in!\n")
    #         print("\n")
    #     else:
    #         print("\nuser does not exist try again")
    #         print("\n")
    # while status != "ex":
    #     displayMenu()
    # if status == 'l':

        while True:
                # print(f"welcome {u_name}.")
                print("Use these short codes : create - create a new password locker account, login - if you are already a user,  logout -log out of your account ")
                short_code = input().lower()
                if short_code == 'create':
                    print('enter your first name')
                    first_name = input()
                    print("-"*40)

                    print('enter your last name')
                    last_name = input()
                    print("-"*40)


                    print('enter your user name')
                    user_name = input()
                    print("-"*40)

                    print('enter your email')
                    email = input()
                    print("-"*40)

                    print('enter your password')
                    password = input()
                    print("-"*40)

                    save_user(create_user(first_name,last_name,user_name,email,password))
                    print(f'{welcome user_name }')

                    print ('\n')
                        print(f"Here are your account details....{first_name}......{last_name}.....{user_name}....{email}......{password}created")
                        print ('\n')

                elif short_code == 'login'
                    print('Welcome back. To login please enter your details')
        			email = input('Enter your email')
        			password = input('Enter your password')


                    print('enter a secret key')
                    s_name = input()
                    print("-"*40)
                elif short_code == 'dc':

                            if display_credentials():
                                    print("here is a list of your accounts")
                                    print("-"*40)

                                    for credential in display_credentials():
                                            print(f"{credential.a_name}......{user.pass_name} .....{user.s_name}")

                                    print("-"*40)
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print("-"*40)


                # elif short_code == 'sc':
                #
                #     secretkey = input("Enter the password you want to search for")
                #     if check_existing_credentials(secretkey):
                #             search_credential = find_credential(secretkey)
                #             print(f"{search_credential.account} {search_credential.password}")
                #             print('-' * 40)
                #
                #             print(f"password.......{search_credential.account}")
                #             print(f"Email address.......{search_credential.password}")
                #     else:
                #             print("That accoun does not exist")
                #

                elif short_code == "ex":
                            print("logging out")
                            break
                else:
                            print("try again. Please use the short codes")





if __name__ == '__main__':

    main()
