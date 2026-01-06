password=input("Enter password:")
length=len(password)

if length>=8:
    print("Strong password")
elif length>=5:
    print("Medium")
else:
    print("Weak password")
