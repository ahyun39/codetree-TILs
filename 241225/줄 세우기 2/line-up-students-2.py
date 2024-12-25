class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

students = []

for i in range(int(input())):
    h, w = map(int, input().split())
    students.append(Student(h,w,i+1))

students.sort(key=lambda x:(x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.idx)