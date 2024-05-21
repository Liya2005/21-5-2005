def check_insurance_eligibility(married, gender, age):
    if married:
        return True
    elif gender == 'male' and age > 30:
        return True
    elif gender == 'female' and age > 25:
        return True
    else:
        return False
married_status = input("Is the driver married? (yes/no): ").lower() == 'yes'
gender = input("Enter driver's gender (male/female): ").lower()
age = int(input("Enter driver's age: "))

if check_insurance_eligibility(married_status, gender, age):
    print("The driver is eligible for insurance coverage.")
else:
    print("The driver is not eligible for insurance coverage based on the given criteria."
