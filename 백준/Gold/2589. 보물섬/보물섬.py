from collections import deque
import sys
input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(sx, sy):
    queue = deque([(sx, sy)])
    visited = [[-1] * C for _ in range(R)]  # 방문 배열 및 거리 저장
    visited[sy][sx] = 0  # 시작점 거리 0
    max_dist = 0

    while queue:
        x, y = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and visited[ny][nx] == -1 and graph[ny][nx] == 'L':
                visited[ny][nx] = visited[y][x] + 1
                max_dist = max(max_dist, visited[ny][nx])  # 최대 거리 갱신
                queue.append((nx, ny))

    return max_dist

# 입력 처리
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

# 가장 긴 거리 계산
longest = 0
for y in range(R):
    for x in range(C):
        if graph[y][x] == 'L':  # 육지인 경우에만 BFS 실행
            longest = max(longest, bfs(x, y))

print(longest)


