def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
num = int(input("entre a number: "))
print(f"The factorial of {num} is {factorial(num)}")