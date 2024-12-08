class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []

for _ in range(int(input())):
    n, h, w = map(str, input().split())
    students.append(Student(n, int(h), int(w)))

students.sort(key=lambda x:(x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)