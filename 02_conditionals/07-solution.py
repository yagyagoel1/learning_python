coffeeSize=input("enter the size of the coffee: ")
options=int(input("enter the options enter 1 for extra shot or 2 for expresso enter any other no for none : "))

if options==1:
    coffee = coffeeSize + " coffee with extra shot"
elif options==2:
    coffee = coffeeSize + " coffee with expresso"
else:
    coffee = coffeeSize + " coffee"



print("You ordered a ", coffee)
