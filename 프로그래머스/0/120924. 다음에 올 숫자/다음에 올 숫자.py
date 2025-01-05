def solution(common):
    answer = 0
    n=len(common)
    diff = common[1]-common[0]
    if common[2]-common[1]==diff:
        answer = common[n-1]+diff
    else:
        answer = common[n-1]*(common[1]/common[0])
    return answer