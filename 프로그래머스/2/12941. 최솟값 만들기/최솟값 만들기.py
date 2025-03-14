def solution(A, B):
    answer = 0
    A_sort = sorted(A)              
    B_sort = sorted(B, reverse=True)  
    for x, y in zip(A_sort, B_sort):
        answer += x * y
    return answer