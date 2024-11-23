n, k, T = map(str, input().split())
words = []
for _ in range(int(n)):
    word = str(input())
    if len(word) >= len(T):
        if word[:len(T)] == T:
            words.append(word)
words.sort()
print(words[int(k)-1])