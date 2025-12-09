import sys
input = sys.stdin.readline

K, L = map(int, input().split())

last_order = {}  # 학번 -> 마지막 클릭 순서

for i in range(L):
    student = input().strip()
    last_order[student] = i  # 같은 학번이 다시 나오면 값이 갱신됨 (맨 뒤로 밀리는 효과)

# (학번, 마지막 클릭 순서) 튜플들을 '클릭 순서' 기준으로 정렬
sorted_students = sorted(last_order.items(), key=lambda x: x[1])

cnt = 0
for student, _ in sorted_students:
    if cnt == K:
        break
    print(student)
    cnt += 1