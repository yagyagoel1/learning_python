import math as Math
n = int(input("enter a number : "))
if n==2:
    print("The number is prime")
    exit() 
for i in range(2,int(Math.sqrt(n)+1)):
    if n%i==0:
        print("The number is not prime")
        break
print("The number is prime")