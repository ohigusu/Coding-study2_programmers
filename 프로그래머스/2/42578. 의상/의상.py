from collections import defaultdict
def solution(clothes):
    answer = 1
    appendix = {}
    for i in range(len(clothes)):
        kind = clothes[i][1]
        if kind in appendix:
            appendix[kind] += 1
        else:
            appendix[kind]=2
    for _,val in appendix.items():
        answer *= val
    answer -= 1
    return answer