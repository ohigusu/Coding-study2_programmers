import math
def solution(arrayA, arrayB):
    gA,gB = arrayA[0],arrayB[0]
    for x in arrayA[1:]:
        gA = math.gcd(gA,x)
    for x in arrayB[1:]:
        gB = math.gcd(gB,x)
    
    def get_max(g,other):
        divs = set()
        for i in range(1,int(g**(1/2))+1):
            if g%i==0:
                divs.add(i)
                divs.add(g//i)
        for d in sorted(divs,reverse=True):
            if d == 1:
                continue
            if all(x%d != 0 for x in other):
                return d
        return 0
    return max(get_max(gA,arrayB),get_max(gB,arrayA))
    
            