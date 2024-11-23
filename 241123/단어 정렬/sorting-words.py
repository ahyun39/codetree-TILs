n = int(input())
words = [str(input()) for _ in range(n)]
words.sort()
print(*words, sep='\n')