def solution(t, p):
    answer, i = 0, 0
    n1, n2 = len(t), len(p)

    for i in range(n1-n2+1):
        if int(t[i:i+n2]) <= int(p):
            answer += 1
        i += 1
    return answer