def solution(dartResult):
    answer,i = 0,0
    score = []
    pa = True
    area = ['S', 'D', 'T']
    for k in range(len(dartResult)):
        dart = dartResult[k]

        if pa:
            if dart in area: 
                score[i - 1] = score[i - 1] ** (area.index(dart)+1)
                
            elif dart in ['*', '#']:
                if dart == '*':
                    if i == 1:
                        score[i - 1] *= 2
                    else:
                        for j in range(i - 2, i):
                            score[j] *= 2
                else: 
                    score[i - 1] *= -1

            else:  
                if dart == '1' and dartResult[k + 1] == '0':
                    pa = False
                    score.append(10)
                else:
                    score.append(int(dart))
                i += 1

        else:
            pa = True  
    answer = sum(score)
    return answer
