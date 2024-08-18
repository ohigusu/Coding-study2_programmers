def solution(n, k):
    if n < 10:
        answer = 12000*n + 2000*k
    else:
        service = n // 10
        answer = 12000*n + 2000*(k-service)
    return answer