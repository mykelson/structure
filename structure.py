#space for students
students = []

#prompt for students' name and dorm
for i in range(3):
    name = input("Name: ")
    dorm = input("Dorm: ")

    #assign each name and dorm to keys in a dict
    student = {"name": name, "dorm": dorm}

    # add each student info to the list
    students.append(student)

#print students' names and dorm
print()

for student in students:
    print(f"{student['name']} is in {student['dorm']}")