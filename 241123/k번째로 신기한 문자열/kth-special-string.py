n, k, T = map(str, input().split())
words = []
for _ in range(int(n)):
    word = str(input())
    if T in word:
        words.append(word)
words.sort()
print(words[int(k)-1])