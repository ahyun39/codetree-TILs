q = int(input())

snum = 0

for _ in range(q):
    command = input()

    if command.startswith("add"):
        _, x = tuple(command.split())
        x = int(x)

        if ((snum >> x) & 1) == 0:
            snum ^= (1 << x)

    elif command.startswith("delete"):
        _, x = tuple(command.split())
        x = int(x)

        if ((snum >> x) & 1) == 1:
            snum ^= (1 << x)
        
    elif command.startswith("print"):
        _, x = tuple(command.split())
        x = int(x)

        print(((snum >> x) & 1))
    
    elif command.startswith("toggle"):
        _, x = tuple(command.split())
        x = int(x)

        snum ^= (1 << x)

    else:
        snum = 0