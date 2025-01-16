def solution(s):
    lower_chars = sorted([ch for ch in s if ch.islower()],reverse=True)
    upper_chars = sorted([ch for ch in s if ch.isupper()],reverse=True)
    return ''.join(lower_chars + upper_chars)