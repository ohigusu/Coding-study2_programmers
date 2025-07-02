from collections import deque

def solution(n, computers):
    visited = [False] * n

    # BFS로 하나의 네트워크(연결 요소)를 통째로 방문 처리
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            curr = queue.popleft()
            for v in range(n):
                if computers[curr][v] == 1 and not visited[v]:
                    visited[v] = True
                    queue.append(v)

    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)   # dfs[i] → bfs(i) 로 수정
            cnt += 1

    return cnt