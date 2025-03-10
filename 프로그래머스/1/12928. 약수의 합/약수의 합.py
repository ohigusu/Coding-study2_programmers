def solution(n):
    if n == 0: 
        return 0
    answer = 0
    for i in range(1, int(n**0.5) + 1):  
        if n % i == 0:  
            answer += i  
            if i != n // i:  
                answer += n // i
    return answer
