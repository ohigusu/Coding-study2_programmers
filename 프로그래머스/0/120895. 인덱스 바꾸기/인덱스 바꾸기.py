def solution(my_string, num1, num2):
    answer = ""
    char1,char2 = my_string[num1],my_string[num2]
    idx = 0
    for char in my_string:
        if idx == num1:
            answer += char2
        elif idx == num2:
            answer += char1
        else:
            answer += char
        idx += 1
    return answer