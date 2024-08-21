n, t = map(int,input().split())
belt = list(map(int,input().split())) + list(map(int,input().split()))
t %= len(belt)

belt = belt[-t:] + belt[:-t]

print(*belt[:n])
print(*belt[n:])