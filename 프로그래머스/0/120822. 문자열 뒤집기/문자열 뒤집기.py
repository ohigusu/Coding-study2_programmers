#sol1:
def solution(my_string):
    return my_string[::-1]
#sol2:
def solution(my_string):
    answer = ''
    for i in range(len(my_string)-1, -1, -1) :
        answer += my_string[i]
    return answer
#sol3:
def solution(my_string):
    return ''.join(reversed(my_string))
