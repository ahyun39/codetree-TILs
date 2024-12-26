a, b, c = map(int, input().split())
minutes = 0

na, nb, nc = 11, 11, 11
while True:
    if (na, nb, nc) == (a, b, c):
        break
    
    nc += 1
    minutes += 1

    if nc == 60:
        nb += 1
        nc = 0
        if nb == 24:
            na += 1
            nb = 0

print(minutes)