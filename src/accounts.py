#this file contains code for managing my account
accounts = {}
#function that adds user details to accounts

def add_account(name, password):
   """
   Adds the key value pair to the accounts dictionaries
   """
   name = input("Choose a Username: ")#creating a placeholder for username
   password = input("Choose a password: ")

   if  name.isalpha() == False:
       print(" username should contain only alphabetic letters") 
   else:
       accounts[password] = name
       return accounts
       


def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    my_password = password
    my_name = name
    if my_password in accounts and my_name in accounts == accounts[my_password]:
        print("You have been logged in")
        return True
    else:
        print("Create an account")
        return False
    
login("name", "password")
