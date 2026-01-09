customers = {
    1: {"name": "Arun", "email": "arun@gmail.com", "status": "Lead"},
    2: {"name": "Meera", "email": "meera@gmail.com", "status": "Customer"}
}

while True:
    print("\n CRM DRIVEN gitMENU")
    print("1. Display All Customers")
    print("2. Add New Customer")
    print("3. Update Customer Status")
    print("4. Search Customer")
    print("5. Delete Customer")
    print("6. Display Customers by Status")
    print("7. Count Customers by Status")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display
    if choice == 1:
        for cid, details in customers.items():
            print("\nID:", cid)
            print("Name:", details["name"])
            print("Email:", details["email"])
            print("Status:", details["status"])
            print("-----------------------------")

    # 2. Add
    elif choice == 2:
        cid = int(input("Enter Customer ID: "))

        if cid in customers:
            print("ID already exists!")
        else:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            status = input("Enter Status (Lead/Customer/Client): ")

            email_exists = False
            for c in customers:
                if customers[c]["email"] == email:
                    email_exists = True

            if email_exists:
                print("Email already exists!")
            else:
                customers[cid] = {
                    "name": name,
                    "email": email,
                    "status": status
                }
                print("Customer added successfully")

    # 3. Update Status
    elif choice == 3:
        cid = int(input("Enter Customer ID: "))

        if cid in customers:
            current_status = customers[cid]["status"]

            if current_status == "Lead":
                customers[cid]["status"] = "Customer"
                print("Status updated to Customer")

            elif current_status == "Customer":
                customers[cid]["status"] = "Client"
                print("Status updated to Client")

            else:
                print("Already Client. No downgrade allowed")
        else:
            print("Customer ID not found")

    # 4. Search
    elif choice == 4:
        search = input("Enter Customer ID or Email: ")
        found = False

        for cid, details in customers.items():
            if str(cid) == search or details["email"] == search:
                print("\nID:", cid)
                print("Name:", details["name"])
                print("Email:", details["email"])
                print("Status:", details["status"])
                print("-----------------------------")
                found = True
                break

        if not found:
            print("Customer not found")

    # 5. Delete
    elif choice == 5:
        cid = int(input("Enter Customer ID to delete: "))

        if cid in customers:
            if customers[cid]["status"] == "Lead":
                del customers[cid]
                print("Customer deleted successfully")
            else:
                print("Cannot delete active customer")
        else:
            print("Customer ID not found")

    # 6. Display by Status
    elif choice == 6:
        status_input = input("Enter Status (Lead/Customer/Client): ")
        found = False

        for cid, details in customers.items():
            if details["status"] == status_input:
                print("\nID:", cid)
                print("Name:", details["name"])
                print("Email:", details["email"])
                print("Status:", details["status"])
                print("-----------------------------")
                found = True

        if not found:
            print("No customers found with this status")

    # 7. Count
    elif choice == 7:
        lead_count = 0
        customer_count = 0
        client_count = 0

        for cid, details in customers.items():
            if details["status"] == "Lead":
                lead_count += 1
            elif details["status"] == "Customer":
                customer_count += 1
            elif details["status"] == "Client":
                client_count += 1

        print("Leads:", lead_count)
        print("Customers:", customer_count)
        print("Clients:", client_count)

    # 8. Exit
    elif choice == 8:
        print("Exit")
        break

    else:
        print("Invalid choice!")
