import sys
input = sys.stdin.readline

left = list(input().strip())  # 초기 문자열
right = []

n = int(input())

for _ in range(n):
    command = input().strip()
    if command[0] == 'P':
        _, ch = command.split()
        left.append(ch)
    elif command == 'L':
        if left:
            right.append(left.pop())
    elif command == 'D':
        if right:
            left.append(right.pop())
    elif command == 'B':
        if left:
            left.pop()

# 왼쪽 + 오른쪽 뒤집은 것 이어붙이기
print(''.join(left + right[::-1]))
