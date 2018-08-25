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

    users = {}
    status = ""
    def displayMenu():
        status = input("welcome to the master password please sign up by pressing s to or  login by pressing l \n" )
        print("-"*40)
        if status == "l":
            oldUser()
        elif status == "s":
            newUser()
        else:
                print('incorrect input please try again')

    def newUser():
        f_name = input("firstname \n")
        print("-"*40)

        l_name = input("lastname \n")
        print("-"*40)

        u_name = input("username \n")
        print("-"*40)

        email = input("email \n")
        print("-"*40)

        p_name = input("password \n")
        print("-"*40)

        if u_name in users:
            print("\n username already\n")
            print("\n")
        else:
            p_name = input("password")
            users[u_name] = p_name
            print("\n User registered\n")

    def oldUser():
        u_name = input ("enter username")
        p_name = input ("enter password")

        if u_name in users and users[u_name] == p_name:
            print("\nyou are logged in!\n")
            print("\n")
        else:
            print("\nuser does not exist try again")
            print("\n")

        while True:
                print(f"welcome {u_name}.")

                print("Use these short codes : ca - create a new account, dc - display account, fc -find a account, ex -exit the account list ")
                short_code = input().lower()
                if short_code == 'ca':
                    print('enter account name')
                    a_name = input()
                    print("-"*40)

                    print('enter the account password')
                    pass_name = input()
                    print("-"*40)

                    print('enter a secret key')
                    s_name = input()
                    print("-"*40)
                elif short_code == 'dc':

                            if display_credentials():
                                    print("here is a list of your accounts")
                                    print("-"*40)

                                    for credential in display_credentials():
                                            print(f"{credential.account}......{user.password} .....{user.secretkey}")

                                    print("-"*40)
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print("-"*40)

                elif short_code == "ex":
                            print("logging out")
                            break
                else:
                            print("try again. Please use the short codes")

    while status != "ex":
            displayMenu()


if __name__ == '__main__':

    main()
