# conditonal statment

# if condition:
#   pass

#elif condition:
#   pass

# else:
#   pass

my_discts ={
    "1":"ram",
    "2":"hari"
}
my_keys=my_discts.keys() #("1","2")
my_values=my_discts.values()#("ram","hari"511)

roll_no=input("enter roll no:")

if roll_no in my_keys:
    print("key already existed")

else:
    name=input("enter name:")
    if name in my_values:
        print("name already existed")
    else:

         my_discts.update(
         roll_no=name
    )
    print("student",my_discts)

    