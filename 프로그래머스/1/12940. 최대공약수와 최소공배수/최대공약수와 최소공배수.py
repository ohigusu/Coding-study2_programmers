def solution(n, m):
    answer,store = [],[]
    small, large = min(n,m), max(n,m)
    for i in range(1,int(small**0.5)+1):
        if small%i == 0:
            store.append(i)
            if (small//i) != i:
                store.append(small//i)
    gcd = max(j for j in sorted(store, reverse=True) if large % j == 0)
    answer.append(gcd)
    # 최소공배수(lcm) = m*n/최대공배수(gcd)
    answer.append(m*n/gcd)
    return answer

# if b % a == 0 or a % b == 0:
#         return [a,b]

#     if b > a and b % a != 0:
#         return [b%a,b*a]

#     if a > b and a % b != 0:
#         return [a%b,a*b]