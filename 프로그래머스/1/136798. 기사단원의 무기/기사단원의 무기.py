def solution(numbers, limit, power):
    answer = 0
    for num in range(1,numbers+1):
        count = 0
        sqrt_n = int(num**0.5) + 1
        for i in range(1, sqrt_n):
            if num % i == 0:
                count += 1 
                if i != num // i: 
                    count += 1
        if count > limit:
            answer += power
        else:
            answer += count
    return answer