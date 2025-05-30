N = int(input())
levels = [int(input()) for _ in range(N)]
max_point = levels[-1]
result = 0
for i in range(N-2,-1,-1):
    if levels[i] >= max_point:
        result += levels[i]-max_point+1
        max_point -= 1
    else:
        max_point = levels[i]
print(result)