N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    cnt = 1
    visited[y][x] = 1
    for i in range(4):
        nx,ny = x + dx[i],y+dy[i]
        if 0<= nx < N and 0<= ny < N:
            if graph[ny][nx]==1 and not visited[ny][nx]:
                cnt += dfs(nx,ny)
    return cnt

result = []

for i in range(N):
    for j in range(N):
        if graph[j][i]==1 and not visited[j][i]:
            result.append(dfs(i,j))

print(len(result))
for r in sorted(result):
    print(r)
