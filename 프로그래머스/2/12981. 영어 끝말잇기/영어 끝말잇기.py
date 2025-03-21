def solution(n, words):
    answer = [0,0]
    for idx, word in enumerate(words):
        if idx > 0:
            pre_word = words[idx - 1]
            if (word in words[:idx]) or (pre_word[-1] != word[0]) or (len(word) < 2):
                person = idx % n + 1
                turn = idx // n + 1
                return [person, turn]
        else:
            if len(word) < 2:
                return [1, 1] 
    return answer