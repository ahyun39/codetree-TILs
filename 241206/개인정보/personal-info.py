class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []

for _ in range(5):
    n, h, w = map(str, input().split())
    students.append(Student(n, int(h), float(w)))

def printf(students):
    for student in students:
        print(student.name, student.height, student.weight)

students.sort(key=lambda x:x.name)

print("name")
printf(students)

print()

students.sort(key=lambda x:-x.height)

print("height")
printf(students)