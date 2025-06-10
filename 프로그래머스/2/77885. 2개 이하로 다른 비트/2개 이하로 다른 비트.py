def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            answer.append(x+1)
        else:
            bit = (x ^ (x + 1)) >> 2
            answer.append(x + bit + 1)
        
    return answer