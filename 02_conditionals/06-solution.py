distance= int(input("Enter the distance in km: "))


if distance < 3:
    transport= "Walk"
elif distance <= 15:
    transport= "Bike"
else:
    transport= "Bus"




print("You should take a ", transport)