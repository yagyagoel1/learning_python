def print_kargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kargs(name="john", age=25, city="New York")
print_kargs(name="john", age=25)
print_kargs(name="john")