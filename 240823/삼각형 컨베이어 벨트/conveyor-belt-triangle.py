from collections import deque

n, t = map(int,input().split())
graph = list(map(int,input().split())) + list(map(int,input().split())) + list(map(int,input().split()))
graph = deque(graph)
graph.rotate(t)
graph = list(graph)
print(*graph[:n])
print(*graph[n:2*n])
print(*graph[2*n:])