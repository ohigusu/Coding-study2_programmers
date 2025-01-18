def solution(sizes):
    answer = 0
    pre_ma = max(sizes[0][0],sizes[0][1]) #60
    pre_mi = min(sizes[0][0],sizes[0][1]) #50
    #[80,70,60,50,30,40]
    for size in sizes:
        n1, n2 = size
        ma, mi = max(n1,n2),min(n1,n2)
        pre_ma = max(pre_ma,ma)
        pre_mi = max(pre_mi,mi)
    answer = pre_ma*pre_mi
    return answer