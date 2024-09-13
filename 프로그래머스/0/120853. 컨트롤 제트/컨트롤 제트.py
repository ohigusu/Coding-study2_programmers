def solution(s):
    store = []
    for char in s.split(' '):
        if char == 'Z':
            store.pop()
        else:
            store.append(int(char))
    answer = sum(store)
    return answer
