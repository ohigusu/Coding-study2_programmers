from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    grid = [list(row) for row in maps]
    
    start = lever = exit_ = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':      start = (i, j)
            elif grid[i][j] == 'L':    lever = (i, j)
            elif grid[i][j] == 'E':    exit_ = (i, j)
    
    # BFS
    def bfs(sx, sy, tx, ty):
        dist = [[-1]*m for _ in range(n)]
        q = deque()
        q.append((sx, sy))
        dist[sx][sy] = 0
        
        while q:
            x, y = q.popleft()
            if (x, y) == (tx, ty):
                return dist[x][y]
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if dist[nx][ny] == -1 and grid[nx][ny] != 'X':
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        return -1
    
    # 시작→레버, 레버→출구 최단 거리 계산
    d1 = bfs(start[0], start[1], lever[0], lever[1])
    if d1 == -1:
        return -1
    
    d2 = bfs(lever[0], lever[1], exit_[0], exit_[1])
    if d2 == -1:
        return -1
    
    return d1 + d2

