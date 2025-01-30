def solution(dartResult):
    answer = 0
    i = 0
    score = []
    pa = True

    for k in range(len(dartResult)):
        dart = dartResult[k]

        if pa:
            if dart in ['S', 'D', 'T']:
                if dart == 'S':
                    pass
                elif dart == 'D':
                    score[i - 1] = score[i - 1] ** 2
                else:  
                    score[i - 1] = score[i - 1] ** 3

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
