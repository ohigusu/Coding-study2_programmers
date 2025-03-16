import sys
N = int(sys.stdin.readline())
stack = [0]
for _ in range(N):
	word = sys.stdin.readline().strip()
	if int(word)==0:
		stack.pop()
	else:
		stack.append(int(word))
print(sum(stack))
