def solution(n, m, section):
    answer = 1
    ma,mi = section[-1],section[0]
    if (ma-mi)+1 <= m: 
        return answer
    elif (ma-mi)+1 > m:
        pass_i = mi + m - 1
        for i in section:
            if i > pass_i:
                pass_i = i+m-1
                answer += 1
    return answer