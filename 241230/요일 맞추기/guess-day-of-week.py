m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
day = 1

if (m1, d1) < (m2, d2):
    while True:
        if m1 == m2 and d1 == d2:
            break
        
        d1 += 1
        day += 1

        if d1 > num_of_days[m1]:
            d1 = 1
            m1 += 1
        
        if day >= 7:
            day = 0

else:
    while True:
        if m1 == m2 and d1 == d2:
            break
        
        d1 -= 1
        day -=1 

        if d1 < 1:
            m1 -= 1
            d1 = num_of_days[m1]

        if day < 0:
            day = 6
    
print(day_of_week[day])