m1, d1, m2, d2 = map(int, input().split())
A = input()

dayofweek = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nday = 0
A_cnt = 0

while True:

    if m1 == m2 and d1 == d2:
        break

    d1 += 1
    nday += 1

    if nday > 6:
        nday = 0
    
    if dayofweek[nday] == A:
        A_cnt += 1

    if d1 > num_of_days[m1]:
        d1 = 1
        m1 += 1

print(A_cnt)
