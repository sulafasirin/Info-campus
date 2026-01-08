def check_eligibility(age):
    if age>= 18:
        return "Eligible"
    else:
        return "Not eligible"
    
age=int(input("Enter age:"))
print(check_eligibility(age))