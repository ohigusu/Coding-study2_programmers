import sys

brackets = sys.stdin.readline().strip()
stack = []
result = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if brackets[i - 1] == '(': 
            result += len(stack)
        else:
            result += 1

print(result)
