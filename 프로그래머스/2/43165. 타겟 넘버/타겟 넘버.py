def solution(numbers, target):
    answer = 0
    def dfs(idx,now):
        nonlocal answer
        if len(numbers)==idx:
            if now == target:
                answer += 1
            return
        dfs(idx+1,now - numbers[idx])
        dfs(idx+1,now+numbers[idx])
    dfs(0,0)
    return answer