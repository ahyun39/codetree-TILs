class Secret:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

c, p, t = map(str, input().split())

secret = Secret(c, p, t)

print(f'secret code : {secret.code}')
print(f'meeting point : {secret.point}')
print(f'time : {secret.time}')