def solution(num_list):
    answer = num_list[::-1]
    return answer

#sol2
def solution(num_list):
    result =[]
    while(num_list):
        result.append(num_list.pop())
    return result
