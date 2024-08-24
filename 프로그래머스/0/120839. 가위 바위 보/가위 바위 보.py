def solution(rsp):
    answer = ''
    hash = {"2":"0","0":"5","5":"2"}
    for i in rsp:
        answer += hash[i]
    return answer