color =  input("enter the color of the fruit: ")
fruit = input("enter the name of the fruit: ")

if fruit.lower() == "banana":
    if color.lower()== "green":
        print("the fruit is unripe")
    if color.lower()== "yellow":
        print("the fruit is ripe")
    if color.lower()== "brown":
        print("the fruit is overripe")