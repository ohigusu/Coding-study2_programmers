def solution(numbers):
    alpha = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    
    word,result = "",""
    
    for i in numbers:
        word += i 
        if word in alpha:
            result += str(alpha[word])
            word = ""
        else:
            continue

    answer = int(result)
    return answer