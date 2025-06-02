import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# child[i] = 번호 i인 아이의 현재 위치 (인덱스)
pos = [0] * (n + 1)
for i in range(n):
    pos[arr[i]] = i

# 가장 긴 연속 증가하는 위치 찾기
max_len = 1
cur_len = 1

for i in range(2, n + 1):
    if pos[i] > pos[i - 1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1

# 전체 - 가장 긴 연속 증가 순서 = 이동할 아이 수
print(n - max_len)
