N = int(input())
Tops = list(map(int, input().split()))

stack = []  # (인덱스, 높이)
answer = [0] * N

for i in range(N):
    while stack and stack[-1][1] < Tops[i]:
        stack.pop()
        
    if stack:
        answer[i] = stack[-1][0] + 1 
    else:
        answer[i] = 0
        
    stack.append((i, Tops[i]))
print(*answer)
			