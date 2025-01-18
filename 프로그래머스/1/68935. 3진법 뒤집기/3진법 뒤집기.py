def solution(n):
    n_3=[]
    while n>0:
        n_3.append(n%3)
        n//=3
    answer = 0
    for i in range(len(n_3)):
        answer*=3
        answer+=n_3[i]
    return answer
 