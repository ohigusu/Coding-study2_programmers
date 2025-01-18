def solution(s):
    answer = ''
    li = s.split(' ')
    for j,chars in enumerate(li):
        for idx,char in enumerate(chars):
            if idx%2:
                answer += char.lower()
            else:
                answer += char.upper()
        if j != len(li)-1:
            answer += ' '
    return answer