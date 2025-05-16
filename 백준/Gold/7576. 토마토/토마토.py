# 토마토
from collections import deque
import sys
m, n = map(int, input().split())
# M: 상자의 가로 칸의 수
# N: 상자의 세로 칸의 수
tomatoes = [list(map(int, input().split())) for _ in range(n)]
# 정수 1: 익은 토마토, 정수 0: 익지 않은 토마토, 정수 -1: 토마토가 들어있지 않은 칸

dx,dy=[-1,1,0,0],[0,0,-1,1]

queue = deque()
for y in range(n):
    for x in range(m):
        if tomatoes[y][x] == 1:
            queue.append((x, y))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[y][x] + 1
                queue.append((nx, ny))
bfs()
max_days = 0
for x in range(m):
    for y in range(n):
        day = tomatoes[y][x]
        if tomatoes[y][x] == 0:
            print(-1)
            sys.exit(0)
            
        max_days = max(max_days, day)

print(max_days-1)
