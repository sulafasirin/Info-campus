class CRMSystem:
    def __init__(self):
        self.customers=[]
    def add_customer(self):
        cid=int(input("Enter a ID:"))
        name=input("Enter a name:")
        email=input("Enter email:")
        status=input("Enter status(Lead/Customer/Client):")
        print("Customer Added Successfully")
        customer={
            "id":cid,
            "name":name,
            "email":email,
            "status":status
        }
        self.customers.append(customer)
    def display_all(self):
        for c in self.customers:
            print(c)
    
    def search_customer(self):
        s=input("Enter email or ID to search:")
        for c in self.customers:
            if str(c["id"])==s or c["email"]==s:
                print(c)
                
    def update_customer_status(self):
        u=int(input("Enter ID of customer to update:"))
        for c in self.customers:
            if c["id"]==u:
                if c["status"]=="Lead":
                    c["status"]="Customer"
                    print(c)
                elif c["status"]=="Customer":
                    c["status"]="Client"
                    print(c)
                else:
                    print("Cannot downgrade")
                    print(c)
    def delete_customer(self):
        d=int(input("Enter ID to delete:"))
        for c in self.customers:
            if c["id"]==d:
                if c["status"]=="Lead":
                    self.customers.remove(c)
                    print("Customer with ID",c["id"],"removed")
                else:
                    print("Cannot delete customer with status customer or client !!")
    def count_status(self):

        Lead = 0
        Customer = 0
        Client = 0

        for i in self.customers:
            if i["status"] == "Lead":
                Lead += 1

            elif i["status"] == "Customer":
                Customer += 1

            elif i["status"] == "Client":
                Client += 1


        print("\n Count of the Status")

        print("Lead",Lead)
        print("Customer",Customer)
        print("Cleint",Client)


crm=CRMSystem()
while True:
    print("\n---MENU DRIVEN SYSTEM ---")
    print("1. Add Customer")
    print("2. Display All Customers")
    print("3. Search Customer")
    print("4. Update Customer Status")
    print("5. Delete Customer")
    print("6. Count Customers by Status")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        crm.add_customer()
    elif choice == 2:
        crm.display_all()
    elif choice == 3:
        crm.search_customer()
    elif choice == 4:
        crm.update_customer()
    elif choice == 5:
        crm.delete_customer()
    elif choice == 6:
        crm.count_status()
    elif choice == 7:
        print("Exiting CRM System...")
        break
    else:
        print("Invalid choice! Try again.")

        