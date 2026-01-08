def validate_login(username,password):
    if username=="admin" and password=="1234":
        return True
    else:
        return False
    
user_name=input("Enter username:")
user_password=input("Enter password:")

if validate_login(user_name,user_password):
        print("Login successful")
else:
        print("Invalid username or password")