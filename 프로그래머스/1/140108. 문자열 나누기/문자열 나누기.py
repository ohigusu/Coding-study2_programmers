def solution(s):
    answer = 0  
    count_x, count_other = 0, 0  
    first_char = None  
    
    for char in s:
        if first_char is None:
            first_char = char  
        if char == first_char:
            count_x += 1
        else:
            count_other += 1

        if count_x == count_other:
            answer += 1
            first_char = None  
            count_x, count_other = 0, 0 

    if count_x != count_other:
        answer += 1

    return answer