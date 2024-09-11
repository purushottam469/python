# total sum and updaten is dictionaray.

student={"name":"hari","maths":50,"eng":65}
total=0

for  key, value in student.items():
     if key !="name":
        total= total+value,
        print(total)   