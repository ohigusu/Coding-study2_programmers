N = int(input()) 
res = {}

for _ in range(N):
    age, name = input().split()
    age = int(age)
    if age in res:
        res[age].append(name)
    else:
        res[age] = [name]

sorted_res = sorted(res.items())  

for ag, na in sorted_res:
    for i in na:
        print(f"{ag} {i}")
