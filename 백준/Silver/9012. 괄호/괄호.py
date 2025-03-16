import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    word = sys.stdin.readline().strip()
    is_valid = True
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if not stack:
                is_valid = False
                break
            stack.pop()
    if not is_valid or stack:
        print("NO")
    else:
        print("YES")