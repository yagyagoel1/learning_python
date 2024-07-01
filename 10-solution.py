pet = input("enter the pet you have: ")
age = int(input("enter the age of the pet: "))  

if pet.lower() == "dog":
    if age<2:
        print("puppy food")
if pet.lower() == "cat":
    if age>5:
        print("senior cat food")