def solution(order):
    answer = 0
    if order == 0: return answer
    while order > 0:
        num = order % 10
        if num % 3 == 0 and num != 0:
            answer += 1
        order = order//10
    return answer