class User:

    #Class that generates new instances of users
    user_list = [] # Empty user list
    def __init__(self,first_name,last_name,email,username,password,confirmpassword):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword
