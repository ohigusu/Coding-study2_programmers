def solution(progresses, speeds):
    answer = []
    result=[]
    while progresses:
        progress = progresses.pop()
        speed = speeds.pop()
        day = (100-progress)//speed
        if (100-progress)%speed >0:
            day+=1
        result.append(day)
    pre_bepo = result.pop()
    release = 1
    idx = 1
    while result:
        bepo = result.pop()
        if bepo <= pre_bepo:
            release += 1    
        else:
            pre_bepo = bepo
            answer.append(release)
            release = 1
    answer.append(release)
    return answer