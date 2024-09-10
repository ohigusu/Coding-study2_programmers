def solution(n):
    result,answer = 1,1
    while (result <= n):
        answer += 1
        result =  result * answer
    return answer if result == n else answer - 1