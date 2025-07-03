def solution(tickets):
    # 주어진 항공권을 모두 이용 
    # 항상 "ICN" 공항에서 출발
    # 출발지 = 이전 도착지
    # 모든 경로를 확인해야함
    # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로
    n = len(tickets)
    used= [False]*n
    answer = []
    
    def dfs(path,current,used):
        if len(path) == n+1:
            answer.extend(path)
            return True
        
        candidates = [(e,i) for i,(s,e) in enumerate(tickets) if not used[i] and s==current]
        candidates.sort()
        
        for nxt_airport,ti in candidates:
            used[ti]=True
            path.append(nxt_airport)
            if dfs(path,nxt_airport,used):
                return True
            used[ti]=False
            path.pop()
    dfs(["ICN"],"ICN",used)
        
    return answer