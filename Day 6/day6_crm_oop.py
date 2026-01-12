# step 1- Create customer class
class Customer:
    def __init__(self,cid,name,email,status):
        self.cid=cid
        self.name=name
        self.email=email
        self.status=status
    
# step 2-Add Methods
    
    def display(self):
        print(self.cid,self.name,self.email,self.status)
    
    def update(self):
        if self.status=="Lead":
            self.status="Customer"
        elif self.status=="Customer":
            self.status="Client"
        else:
            print("Cannot downgrade")
    def is_deletable(self):
        if self.status=="Lead":
            return True
        else:
            return False
        

c1=Customer(1,"Arun","Arun@gmail.com","Lead")
c2=Customer(2,"Anu","Anu@gmail.com","Customer")

c1.display()
c2.display()
c1.update()
c2.update()
c1.display()
c2.display()
print(c1.is_deletable())

    