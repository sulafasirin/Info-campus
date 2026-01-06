print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Exit")


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ch=int(input("Enter choice:"))


if ch==1:
    res=a+b
    print("sum is:",res)
elif ch==2:
    res=a-b
    print("difference is:",a-b)
elif ch==3:
    res=a*b
    print("multiplication is:",a*b)
elif ch==4:
    print("Exit")
else:
    print("Invalid choice")