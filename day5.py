# for i in range(1,10):
#     append_name=[]
# user_input=input("enter name:")
# append_name.append(user_input)

# user_input=input("do you want to continue")

# if user_input =="n":
#     br
    

# print(f"user-input:{user_input}")

# for i in range(1,10):
#   append_number=[]
#   user_input=input("enter number:")
#   append_number.append(user_input)

#   user_response=input("do yo")


#list of cotumer
ages=[10,20,-3,-10,190,90,180]

#define threshold
threshold=100

#process ages
for age in ages:
    #skip invilid ages
    if age<0:
        continue
    
    #stop loop if age is abovethreshold
    if age>threshold:
       break
    
    #process the valid age
    print(age)





