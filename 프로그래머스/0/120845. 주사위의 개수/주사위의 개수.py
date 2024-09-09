def solution(box, n):
    answer = 1
    answer = answer * (box[0]//n)
    answer = answer * (box[1]//n)
    answer = answer * (box[2]//n)
    return answer