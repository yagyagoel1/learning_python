n=int(input("enter the number: "))

sum_even_no = 0
for i in range(1,n):
    sum_even_no += i if i%2==0 else 0

print("The sum of even numbers is: ", sum_even_no)