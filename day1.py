print("hello world")

name = "Emon"

faculty = "BCA"
dob= "2020-1-20"
age= 4

print("hello" +  name + "is a student of" + faculty + "and your dob is" +dob)

print(f"Type of name: {type(name)}")
print(f"Type of dob: {type(dob)}")
print(f"Type of age: {type(age)}")

name, faculty, dob, age = "meow", "bca", "2020-01-3", 4

x = 9
y = 7

print("before swap: ",x,y)
print("after swap: ",y,x)
x, y = y, x

student_info = ["emon", 4]
name, age = student_info
print("unpacked:", name, age)

name1, *others = student_info
print("name:", name1)
print("others:", others)


student_name = ["Alice", "bob", "charlie", "diana", "demon" ]
student_scores = [2, 90, 3, 4, 5]

print("\nstudent name:", student_name)
print("\nstudent score:", student_scores)

print("\nfirst student:", student_name[0])
print("\nlast student:", student_name[-1])
print("\nfirst three:", student_name[0:3])
print("\nevery student:", student_name[::])
print("\nevery second student:", student_name[::2])

student_name.append('demon')
print("\n after adding demon", student_name)

student_name.insert(1,'demon')
print("\n after adding demon", student_name)

student_name.remove('demon')
print("\n after adding demon", student_name)

passing = [score for score in student_scores if score > 80]

print(passing)

student_record = ("Alice", 20, 85.5, "computer science")
print("Student  Record Tuple:", student_record)

print("name:", student_record[0])
print("age:", student_record[1])


name, age, score, department= student_record
print("\nUnpacked:", name, "is", age, "years old,scored", score, "in", department)

course_A={"Alice", "bob", "charllie", "diana"}
course_B={"charlie", "bob", "eve", "diana"}

print("course a students:", course_A)
print("couesde B students:", course_B)

print("\nintersection:", course_A & course_B)
print("\nunion:",course_A | course_B)
print("\ndiff:" ,course_A - course_B)
print("\nsymmetric diff:", course_A ^ course_B)

print("HILO in course_A:", "HILO"   in course_A)

scores_with_duplicates = [85, 92, 85, 78, 92, 85]
unique_scores = list(set(scores_with_duplicates))
print("\nOriginal scores:", scores_with_duplicates)
print("only in none couorse:", scores_with_duplicates)



print("dictionary -----")

student= {
    "name": "emuu",
    "age" : 21,
    "scores" : [10, 20 , 30],
    "department" : "hm",
    "hobbies": ["sleeping", "eating", "walking", "crying", "shitting"],
    "is_active":True
}

print("student dictionary:")
print(student)

print("studden4t name:", student['name'])
print("studden4t scores:", student['scores'])
print("avhg scores", student['name'])
print("studden4t namde:", student['name'])
print("studden4t hobbbies:", student['hobbies'])


college= {
    "name": "ss college",
    "address": "kirtipur",
    "departments": ["bca", "bba", "bbs"]
}

print("college name:", college['name'])
print("college address:", college['address'])
print("college departments:", college['departments'])

