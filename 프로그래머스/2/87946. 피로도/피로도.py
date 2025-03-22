def solution(k, dungeons):
    # 최소 필요 피로도 : 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
    # 소모 피로도 : 던전을 탐험한 후 소모되는 피로도
    # 오늘 이 던전들을 최대한 많이 탐험
    visited = [False]*len(dungeons)
    max_count = 0

    def dfs(fatigue, count):
        nonlocal max_count
        max_count = max(max_count, count)
        for i in range(len(dungeons)):  # 가능한 선택들: 방문 안한 던전들
            min_req, cost = dungeons[i]
            # 🟥 조건 안 맞으면 백트래킹
            if visited[i] or fatigue < min_req:
                continue  # → 이 선택은 무시하고 다음 선택으로
            # 🟩 현재 상태 저장은 visited, fatigue로 자연스럽게 됨
            visited[i] = True  # 방문 처리 → "선택 적용"
            dfs(fatigue - cost, count + 1)  # 🟦 다음 상태로 재귀 호출
            visited[i] = False  # 🟨 상태 복구 ← 백트래킹 핵심

    dfs(k, 0)
    return max_count


