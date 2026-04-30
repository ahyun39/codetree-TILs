import string

message = str(input())
skey = list(set(str(input())))
alpha = skey + [a for a in list(string.ascii_uppercase) if a not in skey and a != "J"]
key_grid = [alpha[i:i+5] for i in range(0, 25, 5)]

def divide(message):

    def check(message):
        for i in range(0, len(message), 2):
            if i+1 < len(message):
                if message[i] == message[i+1]:
                    return False
        return True

    def add_alpha(message):
        new_message = ""
        for i in range(0, len(message), 2):
            if i+1 < len(message):
                a, b = message[i], message[i+1]
                if a == b:
                    if a != "X":
                        new_message += a + "X" + b
                    elif a == "X":
                        new_message += a + "Q" + b
                    if i+2 < len(message):
                        new_message += message[i+2:]
                        break
                else:
                    new_message += a + b
            else:
                new_message += message[i]
        return new_message

    while True:
        if check(message):
            break
        else:
            message = add_alpha(message)
    if len(message) % 2 != 0:
        message += "X"
        #else: message += "Q"

    return message

def encrypt(new_message, key_grid):
    encrypted = ""
    for i in range(0, len(new_message), 2):
        a, b = new_message[i], new_message[i+1]
        ax, ay, bx, by = 0, 0, 0, 0
        for x in range(5):
            for y in range(5):
                if key_grid[x][y] == a:
                    ax, ay = x, y
                if key_grid[x][y] == b:
                    bx, by = x, y
        if ax == bx:
            ay = (ay + 1) % 5
            by = (by + 1) % 5
        elif ay == by:
            ax = (ax + 1) % 5
            bx = (bx + 1) % 5
        else:
            temp = ay
            ay = by
            by = temp
        encrypted += (key_grid[ax][ay] + key_grid[bx][by])
    return encrypted

new_message = divide(message)
encrypted = encrypt(new_message, key_grid)
print(encrypted)