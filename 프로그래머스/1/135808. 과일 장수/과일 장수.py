def solution(k, m, score):
    score.sort(reverse=True)  
    answer = 0
    n = len(score)
    
    for i in range(m - 1, n, m):
        answer += score[i] * m 

    return answer