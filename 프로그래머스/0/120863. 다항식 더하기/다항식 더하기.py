def solution(polynomial):
    answer = ''
    coefficient= 0
    bias = 0
    sen = list(polynomial.split(' + '))
    for word in sen:
        if 'x' in word:
            if word == 'x':  # 'x' 단독인 경우 계수는 1
                coefficient += 1
            else:
                coefficient += int(word.replace('x', ''))
        else:
            bias += int(word)
    
    # 결과 문자열 생성
    if coefficient > 0 and bias > 0:
        return f"{coefficient if coefficient != 1 else ''}x + {bias}"
    elif coefficient > 0:
        return f"{coefficient if coefficient != 1 else ''}x"
    else:
        return str(bias)