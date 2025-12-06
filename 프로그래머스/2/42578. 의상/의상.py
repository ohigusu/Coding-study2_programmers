def solution(clothes):
    hash = {}
    answer = 1
    for cloth,type in clothes:
        if type in hash:
            hash[type] += 1
        else:
            hash[type] = 1
    for key,value in hash.items():
        answer *= (value+1)
    return answer-1
        