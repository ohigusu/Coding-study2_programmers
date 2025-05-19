expr = input().strip()

# 1) '-' 로 분할
parts = expr.split('-')

# 2) 첫 부분 합
total = sum(map(int, parts[0].split('+')))

# 3) 나머지는 모두 빼기
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)