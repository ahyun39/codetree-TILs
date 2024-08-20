def count_consecutive_segments(graph, n, m):
    count = 0
    for i in range(n):
        segment_length = 1
        previous_value = graph[i][0]
        for j in range(1, n):
            if graph[i][j] == previous_value:
                segment_length += 1
            else:
                segment_length = 1
                previous_value = graph[i][j]
            if segment_length >= m:
                count += 1
                break
    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = count_consecutive_segments(graph, n, m)
transposed_graph = list(zip(*graph))
ans += count_consecutive_segments(transposed_graph, n, m)
print(ans)