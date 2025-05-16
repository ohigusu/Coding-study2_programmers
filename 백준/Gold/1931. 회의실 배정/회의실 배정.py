N = int(input().strip())
meeting = []
for _ in range(N):
    start,end = map(int,input().strip().split())
    meeting.append((start,end))
meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meeting:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)