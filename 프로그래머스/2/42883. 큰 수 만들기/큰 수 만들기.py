def solution(number, k):
    stack = []
    to_remove = k
    
    for digit in number:
        while stack and to_remove > 0 and stack[-1]<digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    if to_remove:
        stack = stack[:-to_remove]
    return ''.join(stack)
