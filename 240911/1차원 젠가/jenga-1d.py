n = int(input())
blocks = [int(input()) for _ in range(n)]
for _ in range(2):
    s, e = map(int,input().split())
    new_blocks = blocks[:s-1] + blocks[e:]
    blocks = new_blocks
print(len(blocks))
print(*blocks, sep='\n')