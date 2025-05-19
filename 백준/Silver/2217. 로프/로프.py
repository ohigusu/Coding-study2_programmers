N = int(input().strip())
weight = []
for _ in range(N):
    weight.append(int(input().strip()))
weight.sort()

max_weight = max(weight)
for idx,value in enumerate(weight):
    max_weight = max(max_weight,value*(N-idx))
print(max_weight)