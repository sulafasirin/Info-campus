balance=5000
withdraw=int(input("Enter the amount"))

if withdraw<=balance:
    print("Successful")
else:
    print("Insufficient balance")