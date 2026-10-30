#list of tuples
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

setSubjects = set()

for tup in info:
    setSubjects.add(tup[1])

print(setSubjects) 

english_students = []

for name, course in info:
    if course == "English":
       english_students.append(name)

print(english_students)

students_dict = {}

for name,course in info:
    if(students_dict.get(name) == None):
        students_dict.update({name : set()})
        students_dict[name].add(course)
    else:
        students_dict[name].add(course)

print(students_dict)