def solution(n):
    answer = 0
    
    for num in range(4,n+1):
        n = 1
        for i in range(2,num+1):
            if num % i == 0:
                n += 1
        if n >= 3:
            answer += 1
    return answer


