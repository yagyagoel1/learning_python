str = input("enter a string : ")

# container = set()
# for i in range(0, len(str)):
#     if(not container.__contains__(str[i] )and i!=0):
#         print(container.__contains__(str[i] ))
#         print("The first non repeating character is: ", str[i])
        # break
    # else:
        # container.add(str[i])


for char in str:
    if str.count(char) == 1:
        print("The first non repeating character is: ", char)
        break
