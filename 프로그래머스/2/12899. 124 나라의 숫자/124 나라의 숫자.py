def solution(n):
    answer = ''
    while n > 0:
        rest = n%3
        if rest == 0:
            answer = '4'+answer
            n = n//3 - 1
        else:
            answer = str(rest)+answer
            n = n//3
    return answer