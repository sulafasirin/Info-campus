class Customer:
    def __init__(self,cid,name,email,status):
        self.cid=cid
        self.name=name
        self.email=email
        self.status=status
    def display(self):
        print(self.cid,self.name,self.email,self.status)
        
    def convert(self):
        if self.status=="Lead":
            self.status="Customer"
        
c1=Customer(1,"Arun","Arun@gmail.com","Lead")
c1.display

