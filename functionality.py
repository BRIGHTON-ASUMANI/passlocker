#!/usr/bin/env python3.6
from Data import User, Credential
import random
import getpass

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


def confirmation_user(email,password):
	'''
	user confirmation
	'''
	confirm_user = User.validate_users(email,password)
	return confirm_user



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
    return Credential.display_credentials()

def display_account():
    '''
    a function to display all credentials for the user
    '''
    return Credential.display_credentials()

def main():
        while True:
                '''
                this is the first part where we deal with the user sign up and login

                '''

                s = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~!"£$%^&*()/*+='
                passlen = 6
                secpass = 4
                print("-"*40)
                print("Use these short codes : create - create a new password locker account, login - if you are already a user,  exit - to exit the app ")
                print("-"*40)
                short_code = input('Enter a shortcode: ').lower()
                if short_code == 'create':
                    print('enter your first name: ')
                    first_name = input()
                    print("-"*40)

                    print('enter your last name: ')
                    last_name = input()
                    print("-"*40)


                    print('enter your user name: ')
                    user_name = input()
                    print("-"*40)


                    print('enter your email: ')
                    email = input()
                    print("-"*40)
                    while True:

                        print('if you wish to use the default password press d else press p to generate your own password\n')
                        passcode = input('plese enter an option to proceed \n').lower().strip()
                        if passcode == 'd':
                            password = "".join(random.sample(s, passlen))
                            break

                        elif passcode == 'p':
                            password = getpass.getpass('enter your password\n')
                            break
                        else:
                            print("-"*40)
                            print('please read the instructions carefully and try again')
                            print("-"*40)
                    save_users(create_user(first_name,last_name,user_name,email,password))
                    print('welcome to password locker' )
                    print ('-'*40)
                    print(f"Here are your account details \n first name:{first_name} \n last_name: {last_name} \n user name: {user_name} \n email address: {email} \n password: {password}")
                    print ('\n')

                elif short_code == 'login':
                        print('Welcome back. To login please enter your details\n')
                        user_name = input('Enter your username: ')
                        password = getpass.getpass('enter your password ')
                        
                        user_logs = confirmation_user(user_name,password)

                        if user_logs == user_name:
                            while True:
                                print("-"*40)
                                print('press c to create an account, d to display your credential, s to search your credential and ex to exit')
                                print("-"*40)
                                ac_code = input('Please enter an account of your choice that you wish to save: ').strip()
                                print("-"*40)
                                if ac_code == 'c':
                                    account = input('enter the account you want to save\n')
                                    print("-"*40)
                                    ac_password = input('enter the password to this account\n')
                                    print("-"*40)
                                    # i am generating a secret-key to be able to such for the account saved
                                    while True:
                                        print("-"*40)
                                        print('you have to create a secret key to be able to view your account.if you wish to create a secret key press sk else press dsk to get a default secret key')
                                        print("-"*40)
                                        secretcode = input('plese enter an option to proceed \n').lower().strip()
                                        if secretcode == 'dsk':
                                            secretkey = "".join(random.sample(s, secpass))
                                            break

                                        elif secretcode == 'sk':
                                            secretkey = input('Enter your secretkey : ').strip()
                                            break
                                        elif secretcode != 'sk' or secretcode != 'dsk' :
                                            break
                                        else:
                                            print('please read the instructions carefully and try again')
                                            break
                                    save_credentials(create_credential(account,ac_password, secretkey))
                                    print(f'here are your account details: \n......{account}\n........{ac_password}\n..........{secretkey}')

                                elif ac_code == 'd':
                                    if display_secretkeys():
                                        print('-'*40)
                                        for credential in display_secretkeys():
                                            print(f'account: {credential.account} \n Account password: {credential.password}\n ')
                                        print('-'*40)
                                    else:
                                        print('\n')
                                        print("No accounts found")
                                        print('\n')

                                elif ac_code == 's':
                                    sec = input('please enter the secret key of the account you want to search for: ')
                                    if check_existing_credentials(sec):
                                        search_secret = find_credential(sec)
                                        print(f'account: {search_secret.account} \n account-password: {search_secret.password}')
                                    else:
                                        print('the account doesn\'t exist')
                                elif ac_code == 'ex':
                                    print('exiting')
                                    break
                        else:
                            print('user doesnt exist please register')
                            print('-'*40)
                elif short_code == 'exit':
                    print ('exitting.....')
                    break

                else:
                    print('\n')
                    print("please follow instructions and put any of the required short codes")
                    


if __name__ == '__main__':

    main()
