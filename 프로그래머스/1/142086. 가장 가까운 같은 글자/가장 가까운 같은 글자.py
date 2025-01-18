def solution(s):
    answer = []
    store = {}
    idx = 0
    for char in s:
        if char not in store:
            answer.append(-1)
        else:
            answer.append(idx-store[char])
        store[char]=idx
        idx += 1
    return answer