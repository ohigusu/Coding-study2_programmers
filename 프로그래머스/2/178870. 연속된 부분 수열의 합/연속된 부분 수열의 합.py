def solution(sequence, k):
    n = len(sequence)
    l,curr_sum = 0,0  
    
    best_len = float('inf')
    best_l, best_r = 0, 0
    
    for r in range(n):
        curr_sum += sequence[r]

        while curr_sum > k and l < r:
            curr_sum -= sequence[l]
            l += 1
        if curr_sum == k:
            length = r - l  
            if length < best_len:
                best_len = length
                best_l, best_r = l, r

    return [best_l, best_r]
    return answer