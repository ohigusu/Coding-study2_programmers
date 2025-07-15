import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0
    heap = [(0, 1)] #(거리,노드)
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return sum(1 for i in range(1, N+1) if dist[i] <= K)