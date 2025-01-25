def solution(n, m, section):
    answer = 1
    ma,mi = section[-1],section[0]
    if (ma-mi)+1 <= m: 
        return answer
    elif (ma-mi)+1 > m:
        if n-ma+1 >= m:
            pass_i = mi+m-1
            for i in section:
                if i <= pass_i:
                    continue
                else:
                    pass_i = i+m-1
                    answer += 1
        elif n-ma+1 < m:
            pass_i = mi+m-1
            for i in section:
                if i <= pass_i:
                    continue
                elif i > pass_i and i+m-1 <= n:
                    pass_i = i+m-1
                    answer += 1
                elif i > pass_i and i+m-1 > n:
                    answer += 1 
                    break
    return answer