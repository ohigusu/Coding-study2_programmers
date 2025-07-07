def solution(storey):
    answer = float('inf')
    
    def dfs(cnt, now):
        nonlocal answer
        
        if cnt >= answer:
            return
        if now == 0:
            answer = min(answer, cnt)
            return
        
        last = now % 10
        rest = now // 10
        
        if last < 5:
            dfs(cnt + last, rest)
        elif last > 5:
            dfs(cnt + (10 - last), rest + 1)
        else: 
            dfs(cnt + 5, rest)      
            dfs(cnt + 5, rest + 1) 
    dfs(0, storey)
    return answer
