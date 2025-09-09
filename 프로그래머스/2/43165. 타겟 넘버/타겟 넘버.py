def solution(numbers, target):
    answer = 0 # 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수
    def dfs(i,acc):
        nonlocal answer
        if i == len(numbers):
            if acc == target:
                answer += 1
            return
        # i번째 숫자를 더하는 경우
        dfs(i + 1, acc + numbers[i])
        # i번째 숫자를 빼는 경우
        dfs(i + 1, acc - numbers[i])
    dfs(0,0)
    return answer 