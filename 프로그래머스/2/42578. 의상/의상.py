def solution(clothes):
    answer = 1
    appendix = {}
    for i in range(len(clothes)):
        kind = clothes[i][1]
        if kind in appendix:
            appendix[kind] += 1
        else:
            appendix[kind] = 2 # +2를 하는 이유는 “입지 않음”까지 포함하기 때문에
    for _,val in appendix.items():
        answer *= val
    answer -= 1 # 전부 "입지 않음"을 했을 경우 제외
    return answer