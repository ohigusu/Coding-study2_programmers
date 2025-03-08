N = int(input()) 
res = {}

for _ in range(N):
    word = input()
    x, y = word.split()
    x, y = int(x), int(y)
    
    if x in res:
        res[x].append(y)
    else:
        res[x] = [y]

sorted_res = sorted(res.items())  

for x, li_y in sorted_res:
    li_y.sort() 
    for y in li_y:
        print(f"{x} {y}") 

