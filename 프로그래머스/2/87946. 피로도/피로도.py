def solution(k, dungeons):
    # 최소 필요 피로도 : 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
    # 소모 피로도 : 던전을 탐험한 후 소모되는 피로도
    # 오늘 이 던전들을 최대한 많이 탐험
    visited = [False] * len(dungeons)
    max_count = 0
    def dfs(fatigue, count):
        nonlocal max_count
        max_count = max(max_count, count)
        for i in range(len(dungeons)):
            min_req, cost = dungeons[i]
            if not visited[i] and fatigue >= min_req:
                visited[i] = True
                dfs(fatigue - cost, count + 1)
                visited[i] = False 
    dfs(k, 0)
    return max_count
