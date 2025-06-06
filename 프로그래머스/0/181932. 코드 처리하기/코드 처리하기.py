def solution(code):
    ret = '' 
    mode = 0
    for idx, char in enumerate(code):
        if char == "1":  
            mode = 1 - mode  
        else:
            if mode == 0 and idx % 2 == 0:  #idx가 짝수인 경우
                ret += char
            elif mode == 1 and idx % 2 == 1:  # idx가 홀수인 경우
                ret += char
    return ret if ret else "EMPTY"