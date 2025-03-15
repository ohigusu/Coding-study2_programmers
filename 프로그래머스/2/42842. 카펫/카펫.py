def solution(brown, yellow):
    #col = mid_c+2
    #row = mid_r+2
    #mid_c*mid_r = yellow
    #col*row = mid_c*mid_r + 2*(mid_c+mid_r)+4=brown+yellow
    mid_r=1
    mid_c=yellow//mid_r
    while mid_c+mid_r != (brown-4)//2:
        mid_r += 1
        if yellow%mid_r==0:
            mid_c = yellow//mid_r   
        else:
            pass
    return [mid_c+2,mid_r+2]