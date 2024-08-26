def solution(num_list, n):
    answer = []
    i = 0
    while i <= len(num_list)-1:
        answer.append(num_list[i:(n+i)])
        i = (n+i)
    return answer