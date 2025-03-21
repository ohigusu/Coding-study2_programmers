def solution(elements):
    n = len(elements)
    elements = elements * 2  
    sum_set = set()
    
    for length in range(1, n + 1):  # 부분 수열 길이
        for i in range(n):  # 시작 인덱스
            sub_sum = sum(elements[i:i + length])
            sum_set.add(sub_sum)
    
    return len(sum_set)
