from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    cnt = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < m and 0 <= y < n and not visited[y][x] and graph[y][x] == 1:
                cnt += 1
                visited[y][x] = True
                queue.append((x, y))
    return cnt

num_pictures = 0
max_area = 0

for y in range(n):  # 세로 먼저 탐색
    for x in range(m):  # 가로 탐색
        if not visited[y][x] and graph[y][x] == 1:
            area = bfs(x, y)
            num_pictures += 1
            max_area = max(max_area, area)

print(num_pictures)
print(max_area)


