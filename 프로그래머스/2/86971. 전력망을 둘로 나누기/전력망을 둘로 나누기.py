from collections import deque

def solution(n, wires):
    answer = n  
    def bfs_count(start, graph):
        visited = [False]*(n+1)
        visited[start]=True
        #seen = {start}
        q = deque([start])
        cnt = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v] :# not in seen:
                    visited[v]=True#seen.add(v)
                    q.append(v)
                    cnt += 1
        return cnt

    # 1) 끊어볼 전선을 하나씩 선택
    for i in range(len(wires)):
        # --- 이 전선만 뺀 새로운 그래프 생성 ---
        graph = {k: [] for k in range(1, n+1)}
        for j, (u, v) in enumerate(wires):
            if i == j:
                continue  # i번째 전선만 빼고
            graph[u].append(v)
            graph[v].append(u)

        # 2) 끊은 전선의 한쪽 끝(u)에서 BFS → 컴포넌트 A 크기
        u, v = wires[i]
        size_a = bfs_count(u, graph)

        # 3) 나머지 컴포넌트 B 크기는 (n - size_a)
        diff = abs(size_a - (n - size_a))

        # 4) 최소 차이 갱신
        if diff < answer:
            answer = diff

    return answer
