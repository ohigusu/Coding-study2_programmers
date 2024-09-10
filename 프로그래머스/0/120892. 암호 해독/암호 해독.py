def solution(cipher, code):
    answer = ''
    num = len(cipher)//code
    for i in range(1,num+1):
        answer += cipher[(code*i)-1]
    return answer