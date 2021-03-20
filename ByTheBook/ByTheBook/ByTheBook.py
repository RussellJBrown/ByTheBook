import json
from LoggingInAbility import NewUser
from LoggingInAbility import LogInUser


Login = "login"
Signup = "sign up"
UserJson = "users.json"

#Login In/Signup button is pressed
def LoginButtonPress():
    userAction = raw_input("Login or Sign Up").Lower()    
    action = True
    with open(UserJson) as f:
        data = json.load(f)
        #Add Functionality for Buttons at a later point
        #Create JSON for Library  
        while action:    
            if userAction is Login:
                LogInUser(data)
                action = False
            if userAction is Signup:
                newUser(data)
                action = False




if __name__ == "__main__":

    loginButton = False
    
    while True:
        if loginButton:
            LoginButtonPress()
        if newRecipe:
            pass

    
 