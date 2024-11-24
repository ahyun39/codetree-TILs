class Person:
    def __init__(self, name, streetcode, local):
        self.name = name
        self.code = streetcode
        self.local = local 
people = []

for _ in range(int(input())):
    people.append(list(map(str, input().split())))

people.sort(key=lambda x:x[0])

person = Person(people[-1][0], people[-1][1], people[-1][2])

print(f'name {person.name}')
print(f'addr {person.code}')
print(f'city {person.local}')