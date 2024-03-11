from collections import deque

moves = [(-1,0),(0,1),(1,0),(0,-1)]

def in_range(nx,ny,h,w):
    return 1 <= nx <= l + 1 - h and 1 <= ny <= l + 1 - w

def try_movement(idx, dir):
    q = deque()
    q.append(idx)
    # 초기화
    for pid in range(1, n+1):
        dmg[pid] = 0 # 데미지 0으로 초기화
        is_moved[pid] = False # 움직임 False로 초기화
        nr[pid] = r[pid] # 초기 위치
        nc[pid] = c[pid]
    is_moved[idx] = True
    while q:
        x = q.popleft()
        # 움직일 위치
        nr[x] += moves[dir][0]
        nc[x] += moves[dir][1]
        # 보드 밖으로 나가는지 체크
        if not in_range(nr[x],nc[x],h[x],w[x]):
            return False
        # 함정/벽 확인
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if board[i][j] == 1:
                    dmg[x] += 1
                if board[i][j] == 2:
                    return False
        for pid in range(1, n+1):
            if is_moved[pid] or k[pid] <= 0: # 이미 움직였거나 체력이 0 이하인 경우
                continue
            if (r[pid] > nr[x] + h[x] - 1) or (nr[x] > r[pid] + h[pid] - 1):
                continue
            if (c[pid] > nc[x] + w[x] - 1) or (nc[x] > c[pid] + w[pid] - 1):
                continue
            is_moved[pid] = True
            q.append(pid)
    dmg[idx] = 0
    return True

def move_piece(idx, move_dir):
    if k[idx] <= 0:
        return 
    if try_movement(idx, move_dir):
        for pid in range(1, n+1):
            r[pid] = nr[pid]
            c[pid] = nc[pid]
            k[pid] -= dmg[pid]

if __name__ == "__main__":
    l, n, q = map(int,input().split())
    max_n = 31
    max_l = 41
    board = [[2]*(l+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(l)] + [[2]*(l+2)]
    init_k = [0 for _ in range(max_n)]
    r, c, h, w, k = [0]*max_n, [0]*max_n, [0]*max_n, [0]*max_n, [0]*max_n
    nr, nc, dmg = [0]*max_n, [0]*max_n, [0]*max_n
    is_moved = [False] * max_n

    for pid in range(1, n+1):
        r[pid], c[pid], h[pid], w[pid], k[pid] = map(int,input().split())
        init_k[pid] = k[pid]

    for _ in range(q):
        idx, d = map(int,input().split())
        move_piece(idx, d)

    ans = sum([init_k[i] - k[i] for i in range(1,n+1) if k[i] > 0])
    print(ans)