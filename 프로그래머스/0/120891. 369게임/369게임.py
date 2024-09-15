def solution(order):
    answer = 0
    while order > 0:
        num = order % 10
        if num % 3 == 0 and num != 0:
            answer += 1
        order = order//10
    return answer
