customer=[]
while True:
    print("1.insert\n2.delete\n3.display\n4.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
     name=input("enter a name:")
     customer.append(name)
    if ch==2:
        name=input("enter name to remove:")
        if name in customer:
            customer.remove(name)
    elif ch==3:
       print(customer)
    elif ch==4:  
       break    
    else:
       print("Invalid choice")   
