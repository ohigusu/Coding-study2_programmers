def solution(sides):
    sides.sort(reverse = True)
    a,b,c = sides[0],sides[1],sides[2]
    if (b+c>a): return 1
    else: return 2