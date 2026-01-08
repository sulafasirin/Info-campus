customer={
   "sulafa":"1234567890",
   "shahidh":"1123435657",
   "rohan":"7856341709",
   "nived":"1234522222"
}

name=input("Enter your name:")
if name in customer:
    print("Phone number:",customer[name])
else:
    print("customer not found")
