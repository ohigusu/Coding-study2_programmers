from collections import deque

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(sx, sy, w, h, grid, visited):
    q = deque([(sx, sy)])
    visited[sy][sx] = True
    while q:
        x, y = q.popleft()
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))
while True:
    w,h = map(int,input().split())
    if w ==0 and h ==0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    islands = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not visited[y][x]:
                bfs(x, y, w, h, grid, visited)
                islands += 1

    print(islands)
