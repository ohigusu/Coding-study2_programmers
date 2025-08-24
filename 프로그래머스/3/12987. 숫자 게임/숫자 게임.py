def solution(A, B):
    A.sort()
    B.sort()
    
    a_ptr = 0  # A 쪽(가장 작은 수부터)
    b_ptr = 0  # B 쪽(가장 작은 수부터)
    win = 0
    
    n = len(A)
    while a_ptr < n and b_ptr < n:
        if B[b_ptr] > A[a_ptr]:
            # 이길 수 있으면 이긴다
            win += 1
            a_ptr += 1
            b_ptr += 1
        else:
            # 못 이기면 B의 가장 작은 카드 버림
            b_ptr += 1
    return win