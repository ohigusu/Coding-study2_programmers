def solution(sizes):
    answer = 0
    pre_ma = max(sizes[0][0],sizes[0][1]) 
    pre_mi = min(sizes[0][0],sizes[0][1]) 
    for size in sizes:
        ma, mi = max(size),min(size)
        pre_ma = max(pre_ma,ma)
        pre_mi = max(pre_mi,mi)
    answer = pre_ma*pre_mi
    return answer