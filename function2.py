#write a while loop that  stimulates menu-driven

NUM1=3
NUM2=3
NUM3=6
def menu():
    print("press\n a=add\n s=sub\n m=multiply\n e=exit")

def ask_user_input():
    user_input= input("select from amenu:")
    return user_input

def add():
    return NUM1+NUM2+NUM3

def sub():
    return NUM1-NUM2-NUM3

def mul():
    return NUM1*NUM2*NUM3

if __name__=="__main__":
    user_input=ask_user_input()
    add_output=sub_output=mul_output=0
    while user_input in("a","s","m"):
        if user_input=="a":
           add_output=add()
        elif user_input=="s":
             sub_output=sub()
        elif user_input=="m":
            mul_output=mul()
        else:
            break
        menu()
        user_input=input("do you want ot continue:")

    print(f"result: \n addition{add_output} \n multiply{mul_output} \n subract{sub_output}")    
    

