class User:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level
user = User()
print(f'user {user.id} lv {user.level}')

user = User("hello", 28)
print(f'user {user.id} lv {user.level}')