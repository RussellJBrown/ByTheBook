
def NewUser(database):
    email = raw_input("Email: ")
    username = raw_input("User Name: ")
    password = raw_input("Password: ")

    if email in database:
        print("Email is ready in user")
        print("Password Recover?")
    
    if username in database:
        print("Username is already taken")

    if password:
        print("Put in password restrictions")

    else:
        database[username] = password
        createUserPage()


def LogInUser(database):

    IncorrectLoginCount = 0
    while IncorrectLoginCount<2:
        emailOrUserName = raw_input("User or Email: ")
        password = raw_input("Password: ")
        if emailOrUserName in database.values():
           expectedPassword = database[emailOrUserName] 
           if expectedPassword is password:
              loadUserProfile()
              return
           else:
              IncorrectLoginCount+=1
              print("Log in failed: " + Incorrect)


    print("To many failed password attempts")
    return

