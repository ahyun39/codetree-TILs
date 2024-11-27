class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []
n = int(input())

for _ in range(n):
    n, h, w = map(str, input().split())
    student = Student(n, h, w)
    students.append([student.name, student.height, student.weight])

students.sort(key=lambda x:x[1])
for student in students:
    print(*student)