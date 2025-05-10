import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])  # (노드, 깊이)
    visited[start] = True
    invite_count = 0

    while queue:
        current, depth = queue.popleft()

        # 깊이가 2를 초과하면 더 이상 탐색하지 않음
        if depth >= 2:
            continue

        # 친구 탐색
        for friend in graph[current]:
            if not visited[friend]:
                visited[friend] = True
                queue.append((friend, depth + 1))
                # 상근이(1번)를 제외한 초대 인원 카운트
                if friend != 1:
                    invite_count += 1

    return invite_count

# 입력 처리
n = int(input().strip())  # 동기의 수
m = int(input().strip())  # 친구 관계의 수

# 친구 관계 그래프 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS를 통해 초대할 인원 수 계산
result = bfs(1, graph, n)

# 결과 출력
print(result)
