def solution(s):
    answer = ''
    capitalize = True 

    for char in s:
        if char == ' ':
            answer += char
            capitalize = True  
        elif capitalize:
            answer += char.upper()
            capitalize = False
        else:
            answer += char.lower()
    return answer