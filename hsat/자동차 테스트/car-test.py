from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
cars = list(map(int, input().split()))
cars.sort()

for _ in range(q):
    m = int(input())
    left = bisect_left(cars, m)
    right = bisect_right(cars, m)
    if left != 0 and right != n and left != right:
        ans = (n - right) * (left)
    else:
        ans = 0
    print(ans)