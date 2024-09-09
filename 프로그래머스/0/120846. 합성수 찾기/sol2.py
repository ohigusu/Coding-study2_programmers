#대부분의 자연수의 약수는 대상의 제곱근 이하의 약수 하나와 제급근 이상의 약수 하나씩 쌍을 이룬다.
# 합성수는 약수 3개 이상이어야 한다. = 대상과 1을 제외하면 약수 1개 이상이어야 한다. 
# => 제곱근을 사용한 대상의 값에서 약수가 1개라도 있으면 합성수라는 것을 알 수 있다.

def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
