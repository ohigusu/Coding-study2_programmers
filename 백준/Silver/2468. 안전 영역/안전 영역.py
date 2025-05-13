N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]
# 물에 잠기지 않는 안전한 영역이 최대로 몇 개
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
dx,dy = [-1,1,0,0],[0,0,-1,1]

def dfs(sx, sy, height):
    stack = [(sx, sy)]
    visited[sy][sx] = True
    while stack:
        nx, ny = stack.pop()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[y][x] and graph[y][x] > height:
                visited[y][x] = True
                stack.append((x, y))
max_safe_area = 0
max_height = max(map(max, graph))

for height in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_area_count = 0
    for x in range(N):
        for y in range(N):
            if not visited[y][x] and height < graph[y][x]:
                dfs(x,y,height)
                safe_area_count += 1
    max_safe_area = max(max_safe_area, safe_area_count)

print(max_safe_area)