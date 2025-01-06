def solution(s):
    
    n = len(s)
    cnt_p = n-len(s.split("p"))
    cnt_P = n-len(s.split("P"))
    cnt_y = n-len(s.split("y"))
    cnt_Y = n-len(s.split("Y"))

    return cnt_p+cnt_P == cnt_y+cnt_Y