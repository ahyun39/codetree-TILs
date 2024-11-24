class User:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level
user = User()
print(f'user {user.id} lv {user.level}')

user_id, user_level = map(str, input().split())

user = User(user_id, user_level)
print(f'user {user.id} lv {user.level}')