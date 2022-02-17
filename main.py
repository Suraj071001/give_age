def check_age_input(age):
    if age < 0 :
        print(f"You are not born yet.\ni think you need to wait {-age} years to be born.")
    elif age > 140 :
        print(f"You seem to be oldest human alive.")

def show_age(age1) :
    """show age after 100 years"""
    age1 = age1 + 100
    print("Your age is " + str(age1) + " years after 100 years")

def specific_age(age) :
    year = int(input("Enter the year : "))
    age = year - 2022 + age
    print(f"Your age is {age} years in {year}")

age1 = int(input("Enter your age : "))
if age1 >1000 :
    age1 = 2022 - age1
check_age_input(age1)

while True :
    choice = int(input("Enter '1' for age after 100 years '2' for age in specific year or 'any number' for exit :"))
    if choice == 1 :
        show_age(age1)
    elif choice == 2 :
        specific_age(age1)
    else :
        break