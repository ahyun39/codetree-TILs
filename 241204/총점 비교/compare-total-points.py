class Student:
    def __init__(self, name, ascore, bscore, cscore):
        self.name = name
        self.ascore = ascore
        self.bscore = bscore
        self.cscore = cscore

student = []

for _ in range(int(input())):
    name, a, b, c = map(str, input().split())
    student.append(Student(name, int(a), int(b), int(c)))

student.sort(key=lambda x: x.ascore + x.bscore + x.cscore)

for stu in student:
    print(stu.name, stu.ascore, stu.bscore, stu.cscore)