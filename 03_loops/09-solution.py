listt = input("enter the number :  ")

container = set()

for element in listt:
    if(container.__contains__(element)):
        print("this list contains duplicate elements")
        break
    else:
        container.add(element)