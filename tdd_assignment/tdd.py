
user_accounts = {}
expected_char = ["!", "@","%", "#", "&", "*", "$", "^"]

numbers = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase

password = "@Jose1"


def register_user(username, email, password):
    """
    This function allows a user register/create an account
    """
    pass


def userprofile(name, age, gender):
    """
    This function enables a user fill in details for their profile
    """
    pass


def add_account(username, password):
   """
   Adds the key value pair to the user_accounts dictionaries above
   """
   pass


def login(username, password):
    """
    returns true if the password and corresponding username exist in the 
    accounts dicitionary
    """
    pass
    

def validate_password(password):
    if not len(password) is >= 4:
        return False, "Password is too short"
    
    for expected_char in expected_chars:
       if not contains_char(password, expected_char):
           return False, "does not contain {0}".format(expected_char)

    for l in password:
		if password[0] in upper or l in lower or l in number:
			return True
		else:
			return False
	
    

def validate_email(email):
    if not email_address.__contains__('@'):
        return False, "Invalid email address"

    if not email_address.__contains__('.'):
        return False, "Invalid email address"

def validate_name(name):
    if  name.isalpha() == False:
       print(" the name should contain only alphabetic letters") 

def validate_usename(username):
    if username.isalpha() == False:
        print("username should contain only alphabetic letters")

    if username == name:
        print("The username should be different from the name")


def validate_age(age):
    if isinstance(age, str) or age == 0:
        return False
    return True

    
    
    

    
    


    