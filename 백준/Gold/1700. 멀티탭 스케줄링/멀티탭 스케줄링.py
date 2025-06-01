N,K = map(int,input().strip().split())
li = list(map(int,input().strip().split()))

plug = []
cnt = 0

for i in range(K):
    current = li[i]
    # 이미 꽂혀 있으면
    if current in plug:
        continue
    # 빈 구멍이 있으면 
    if len(plug) < N:
        plug.append(current)
        continue
    # 교체가 필요한 경우
    # 향후 사용 안 하거나, 가장 늦게 사용되는 것 제거
    farthest_use = -1
    target_idx = -1
    for idx, device in enumerate(plug):
        try:
            next_use = li[i+1:].index(device)
        except ValueError:
            next_use = float('inf')

        if next_use > farthest_use:
            farthest_use = next_use
            target_idx = idx
    plug[target_idx] = current
    cnt += 1
print(cnt)