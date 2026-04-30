N, K = map(int, input().split())
holes = list(map(int, input().split()))

answer = 0

def cover(tape_l):
    tape_c = 1
    tape = tape_l + holes[0] - 1
    for hole in holes:
        if tape_c > K:
            return False
        if hole > tape:
            tape = hole + tape_l - 1
            tape_c += 1
    if tape_c > K:
        return False
    return True


lo, hi = 1, max(holes)
while lo <= hi:
    mid = (lo+hi)//2
    if cover(mid):
        hi = mid - 1
        answer = mid
    else:
        lo = mid + 1

print(answer)
