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


student_name = ("Alice", "bob", "charlie", "diana", "demon" )
student_scores = (2,  3, 4, 5)

print("\nstudent name:", student_name)
print("\nstudent score:", student_scores)

print("\nfirst student:", student_name[0])
print("\nlast student:", student_name[-1])
print("\nfirst three:", student_name[0:3])
print("\nevery student:", student_name[::])
print("\nevery second student:", student_name[::2])

student_name.append('demon')
print("\n after adding demon", student_name)


