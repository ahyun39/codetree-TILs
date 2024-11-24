class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = map(str, input().split())
bomb = Bomb(code, color, second)

print(f'code : {bomb.code}')
print(f'color : {bomb.color}')
print(f'second : {bomb.second}')