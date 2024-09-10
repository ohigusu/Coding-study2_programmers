def solution(n):
    result,answer = 1,1
    while (result <= n):
        answer += 1
        result =  result * answer
    return answer - 1
