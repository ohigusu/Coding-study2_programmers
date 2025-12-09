import sys
input = sys.stdin.readline

def to_min(t):
    hh,mm = map(int,t.split(":"))
    return hh*60 + mm

s,e,q = input().split()
s_time = to_min(s)
e_time = to_min(e)
q_time = to_min(q)

entered = set()
checked = set()
ans = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    t,name = line.split()
    t_time = to_min(t)

    if t_time <= s_time:
        entered.add(name)
    elif e_time <= t_time <= q_time:
        if name in entered and name not in checked:
            ans += 1
            checked.add(name)
print(ans)