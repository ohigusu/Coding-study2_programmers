def solution(sizes):
    mini,maxi = [],[]
    for size in sizes:
        mini.append(min(size))
        maxi.append(max(size))
    return max(mini)*max(maxi)
    #return max(max(x) for x in sizes)*max(min(x) for x in sizes)