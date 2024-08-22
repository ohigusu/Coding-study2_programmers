def solution(emergency):
    answer,hash = [],{}
    sor = sorted(emergency,reverse=True) 
    for i in range(len(sor)):
        hash[sor[i]] = i+1
    for j in range(len(emergency)):
        answer.append(hash[emergency[j]])
    return answer