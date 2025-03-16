import sys

N = int(sys.stdin.readline())
sen = sys.stdin.readline().strip()

value_map = {}
for i in range(N):
    value_map[chr(ord('A') + i)] = int(sys.stdin.readline().strip())

stack = []

for token in sen:
    if token not in ("*", "+", "-", "/"):
        stack.append(value_map[token])  
    else:
        a = stack.pop()
        b = stack.pop()
        if token == "*":
            stack.append(b * a)
        elif token == "+":
            stack.append(b + a)
        elif token == "-":
            stack.append(b - a)
        elif token == "/":
            stack.append(b / a)

print(f"{stack[0]:.2f}")

