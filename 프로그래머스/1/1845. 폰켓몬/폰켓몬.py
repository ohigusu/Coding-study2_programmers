def solution(nums):
    # 가장 많은 종류의 폰켓몬을 선택하는 방법
    answer = 0
    s,n = set(nums),len(nums)
    mid,cnt = n // 2,len(s)
    if cnt < mid:
        answer = cnt
    elif cnt >= mid:
        answer = mid
    return answer