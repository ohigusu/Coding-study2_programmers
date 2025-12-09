import sys
input = sys.stdin.readline
# 8방향 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dx = (-1,-1,0,1,1,1,0,-1)
dy = (0,1,1,1,0,-1,-1,-1)

def dfs(x:int,y:int,cur:int):
    if cur in liked_set:
        count[cur] += 1
    if len(cur) == max_len:
        return
    for d in range(8):
        nx = (x+dx[d])%n
        ny = (y+dy[d])%m
        dfs(nx,ny,cur+grid[nx][ny])

n,m,k = map(int,input().split())
grid = [input().strip() for _ in range(n)]
liked = [input().strip() for _ in range(k)]

liked_set = set(liked)
count = {}
for s in liked:
    count[s] = 0
max_len = max(len(s) for s in liked)
for i in range(n):
    for j in range(m):
        dfs(i,j,grid[i][j])
for s in liked:
    print(count[s])