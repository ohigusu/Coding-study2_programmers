def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        ans = ''
        i = n-1
        while i >= 0:
            if a >= 2**i and b >= 2**i: 
                ans+= '#'
                a -= 2**i
                b -= 2**i
            elif a >= 2**i: 
                ans+= '#'
                a -= 2**i
            elif b >= 2**i: 
                ans+= '#'
                b -= 2**i
            else:
                ans += ' '
            i -= 1 
        answer.append(ans)
    return answer