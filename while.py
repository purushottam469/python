## while loop
append_number=[]
user_input=input("enter number:")
append_number.append(user_input)
while user_input.isdigit():
    print("execute")
    user_input=input("enter number:")
    append_number.append(user_input)

print(append_number)


# list comprehension
[print(i) for i in range[1,10]if i>5]