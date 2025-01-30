def solution(dartResult):
    score = []
    area = {'S': 1, 'D': 2, 'T': 3}
    k = 0
    while k < len(dartResult):
        if dartResult[k:k+2] == '10':
            score.append(10)
            k += 2
        else:
            score.append(int(dartResult[k]))
            k += 1
        
        score[-1] **= area[dartResult[k]]
        k += 1
        
        if k < len(dartResult) and dartResult[k] in ('*','#'):
            if dartResult[k] == '*':
                score[-1] *= 2
                if len(score) > 1: 
                    score[-2] *= 2
            else:
                score[-1] *= -1
            k += 1  
    
    return sum(score)
