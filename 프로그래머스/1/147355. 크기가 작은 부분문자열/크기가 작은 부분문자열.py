def solution(t, p):
    answer, i = 0, 0
    n1, n2 = len(t), len(p)

    if n1 == n2:
         if int(t) <= int(p):
                answer = 1
    else:
        while i <= (n1-n2):
            if int(t[i:i+n2]) <= int(p):
                answer += 1
            i += 1
    return answer