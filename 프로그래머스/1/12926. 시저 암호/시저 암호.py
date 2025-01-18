def solution(s, n):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char != ' ' and char.isalpha():
            idx = alphabet.index(char.lower())
            find = (idx + n) % len(alphabet)  
            if char.islower():
                answer += alphabet[find]
            else:
                answer += alphabet[find].upper()
        else:
            answer += char
    return answer