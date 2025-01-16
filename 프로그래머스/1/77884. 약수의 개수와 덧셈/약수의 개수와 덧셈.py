def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        yak = []
        for j in range(1,int(i**(0.5))+1):
            if i%j == 0 and j not in yak:
                yak.append(j)
                if i//j not in yak:
                    yak.append(i//j)
        if len(yak)%2:
            answer -= i
        else: 
            answer +=i
    return answer
13+14+15+16+17