N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    count = 1
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            result.append(dfs(i, j))

print(len(result))          # 단지 수
for r in sorted(result):    # 단지별 집 수 (오름차순)
    print(r)
