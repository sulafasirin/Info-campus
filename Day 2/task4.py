username="admin"
password="1234"

attempt=3
while attempt>0:
    u=input("Enter username:")
    p=input("Enter password:")

    if u=="admin"and p=="1234":
        print("Login Successful")
        break
    else:
        attempt=attempt-1
        print("attempt left",attempt)
if attempt==0:
    print("Account locked")