def solution(s):
    s = s[1:len(s)-2]
    li_s = s.split("},")
    sets = [set(map(int,i[1:].split(','))) for i in li_s]
    sets.sort(key=len)
    
    result = []
    seen = set()
    for group in sets:
        num = (group - seen).pop()
        result.append(num)
        seen.add(num)
    return result