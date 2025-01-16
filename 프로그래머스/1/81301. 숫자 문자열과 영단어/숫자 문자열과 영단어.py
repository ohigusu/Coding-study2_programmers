def solution(s):
    answer = ''
    if len(s)==0:
        return answer
    li = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    for i in range(len(s)):
        if s[i] in li.keys():
            answer += s[i]
        else:
            for num,name in li.items():
                if s[i:i+2] == name[:2]:
                    answer += num
                    break
    answer = int(answer)
    return answer