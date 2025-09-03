def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    while n > 0:
        now = s//n
        if n > 1:
            answer.append(now)
            s -= now
        else:
            answer.append(s)
        n -= 1

    return answer