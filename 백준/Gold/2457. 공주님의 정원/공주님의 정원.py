import sys

def to_mmdd(m,d):
    return m*100 + d

N = int(input().strip())
flowers = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().strip().split())
    start = to_mmdd(sm, sd)
    end   = to_mmdd(em, ed)
    flowers.append((start, end))

flowers.sort(key=lambda x: (x[0], -x[1]))

need = 301  
target = 1130
idx, best_end, cnt = 0, 0, 0

while need <= target:
    extended = False
    while idx < N and flowers[idx][0] <= need:
        best_end = max(best_end, flowers[idx][1])
        idx += 1
        extended = True
    if not extended or best_end <= need:
        print(0)
        sys.exit()
    need = best_end
    cnt += 1

print(cnt)