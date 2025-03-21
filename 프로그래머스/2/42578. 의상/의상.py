from collections import defaultdict
def solution(clothes):
    answer = 1
    appendix = defaultdict(list)
    for i in range(len(clothes)):
        appendix[clothes[i][1]].append(clothes[i][0])
    for _,val in appendix.items():
        answer *= len(val)+1
    answer -= 1
    return answer