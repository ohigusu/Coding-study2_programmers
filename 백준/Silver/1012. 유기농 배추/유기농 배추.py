import sys
input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, graph, visited, N, M):
    stack = [(x, y)]
    visited[y][x] = True
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 범위 검사와 방문 여부 및 배추 확인
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                stack.append((nx, ny))

# 테스트 케이스 수 입력
T = int(input().strip())
results = []

for _ in range(T):
    M, N, K = map(int, input().strip().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().strip().split())
        graph[y][x] = 1

    cnt = 0
    # 모든 위치를 순회하면서 DFS로 연결 요소 탐색
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y, graph, visited, N, M)
                cnt += 1
    
    results.append(str(cnt))

# 결과 출력
print("\n".join(results))
