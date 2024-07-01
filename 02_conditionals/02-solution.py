age = int(input("enter your age: "))
day = input("enter the day of the week: ")


price =  12 if age>=18 else 8
if day.lower() == "wednesday":
    price = price-2
print("The price is: ", price)