def solution(a, b, n):
    '''
    입력:
        a : 콜라를 받기 위해 마트에 주어야 하는 병 수
        b : 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수
        n : 상빈이가 가지고 있는 빈 병의 개수
    출력:
        상빈이가 받을 수 있는 콜라의 병 수
    '''
    answer = 0
    rest = n
    while rest >= a:
        answer += (rest//a)*b
        rest = (rest//a)*b + (rest%a)
        
    return answer
