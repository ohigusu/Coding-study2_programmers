def solution(hp):
    answer = hp // 5
    rest = hp%5
    answer =  answer + rest//3
    rest = rest%3
    answer = answer + rest
    return answer