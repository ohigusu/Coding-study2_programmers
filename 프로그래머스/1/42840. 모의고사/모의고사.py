def solution(answers):
    answer, dic, pre = [], {}, 0
    dic[1] = [1, 2, 3, 4, 5]
    dic[2] = [2, 1, 2, 3, 2, 4, 2, 5]
    dic[3] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for key, value in dic.items():
        cand = value * (len(answers)//len(value)) + value[:(len(answers)%len(value))]
        cnt = sum(1 for i, j in zip(answers, cand) if i == j)
        
        if cnt > pre:
            pre = cnt
            answer = [key]
        elif cnt == pre:
            answer.append(key)
    
    return answer