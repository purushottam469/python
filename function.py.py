#function:

# def small():
#     print("hello")
#     return"a"

#function with argument
# def add_with_argument(a):
#      pass

# result=small()

# print(result)



#function with required argument.

# def greet_with_name(name):# name is required argument
#     return f"hello,{name}"

# # result=greet_with_name()
# result=greet_with_name('haii')
# print(result)



#greet with defult argument

def greet_with_name(name="ram"):# ram is defult argument.
    return f"hello,{name}"

result=greet_with_name()
print(result)


def greet_with_name(name="ram"):#defult argument.
    return f"hello,{name}"

result=greet_with_name(age="10")
print(result)