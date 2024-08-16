def solution(array):
    hash = {}
    for i in array:
        # key가 존재하지 않을 경우 기본값 0을 반환하여 문제를 해결
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    # 최빈값 후보를 찾기
    max_count = max(hash.values())
    result = [k for k, v in hash.items() if v == max_count]
    
    # 최빈값이 하나만 있는 경우, 그 값을 반환
    if len(result) == 1:
        answer = result[0]
    else:
        # 최빈값이 여러 개 있을 경우, -1 반환
        answer = -1
    
    return answer