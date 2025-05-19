N = int(input().strip())
A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))
idx_B = [[-1] for _ in range(101)]
for idx,value in enumerate(B):
    if idx_B[value][0] == -1:
        idx_B[value] = idx_B[value][1:]
    idx_B[value].append(idx)

A.sort(reverse=True)
result = 0
idx = 0
for i in range(101):
    if -1 not in idx_B[i] and idx < N:
        for j in idx_B[i]:
            value = A[idx]
            result += value*B[j]
            idx += 1
print(result)