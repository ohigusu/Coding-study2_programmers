def solution(my_string):
    answer = ''
    ae = {"a":True, 
          "e":True,
          "i":True,
          "o":True,
          "u":True}
    for char in my_string:
        if char not in ae:
            answer += char
    return answer