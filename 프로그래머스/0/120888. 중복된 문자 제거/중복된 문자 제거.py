def solution(my_string):
    answer = ''
    re = []
    for char in my_string:
        if char not in re:
            answer += char
            re.append(char)
    return answer