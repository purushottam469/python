# dictonary creatio and access.
student_info={
    "name":"ram",
    "age":209,
    "subject":["cs","maths","eng","nep"]
}   
print(student_info["subject"])

#updating scores
student_scores={"alice":85,"bob":78,"charlie":92}

#updating bob score
student_scores["bob"]=82

#updating new student with score
student_scores.update ({
    'diana':'88',
})

print(student_scores)

#COMBINATION = dictonary+updating:
student_info.update(student_scores)
print('student_info')
