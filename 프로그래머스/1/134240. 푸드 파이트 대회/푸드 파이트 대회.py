def solution(food):
    '''
    Input:
        food:수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 
    Output:
        대회를 위한 음식의 배치를 나타내는 문자열  
    '''
    answer = ''
    l = ''
    for idx in range(1,len(food)):
        if food[idx] < 2:
            continue
        else:
            l += str(idx)*(food[idx]//2)
    answer = l+'0'+l[::-1]
    return answer