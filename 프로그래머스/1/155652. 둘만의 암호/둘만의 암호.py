def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha = alpha.replace(sk,'')
    for char in s:
        idx = (alpha.index(char)+index)%len(alpha)
        answer += alpha[idx]
    return answer