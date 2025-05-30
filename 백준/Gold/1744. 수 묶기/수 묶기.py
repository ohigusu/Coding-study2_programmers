N = int(input())
pos,neg = [],[]
ones,zero = 0,0

for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero += 1
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

result = 0

# 양수
for i in range(0, len(pos) - 1, 2):
    result += pos[i] * pos[i+1]
if len(pos) % 2 == 1:
    result += pos[-1]

# 음수
for i in range(0, len(neg) - 1, 2):
    result += neg[i] * neg[i+1]
if len(neg) % 2 == 1:
    if zero > 0:
        zero -= 1
    else:
        result += neg[-1]
# 1
result += ones

print(result)