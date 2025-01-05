def solution(num, total):
    mid = total//num
    if num%2==1:
        answer = [mid]
        now1,now2 = mid,mid
        for _ in range((num-1)//2): 
            now1 -= 1
            answer.append(now1)
            now2 += 1
            answer.append(now2)
    else:
        answer = []
        now3,now4 = mid,mid
        for i in range(num//2):
            answer.append(now3)
            now3 -= 1
            now4 += 1
            answer.append(now4)
    answer.sort()
    return answer