def solution(n):
    if n < 2:
        return 0  
    answer = 1  # 2는 소수
    for i in range(3, n + 1, 2):  # 3부터 홀수만 검사 
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    
    return answer