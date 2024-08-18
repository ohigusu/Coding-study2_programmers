#sol1
def solution(num_list):
    answer,o,e = [],[],[]
    for i in num_list :
        if i%2 == 0: o.append(i)
        else: e.append(i)
    answer.append(len(o))
    answer.append(len(e))
    return answer
#sol2
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
