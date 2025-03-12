import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()
    
    # 2단계: 허용된 문자만 남김 (소문자, 숫자, -, _, .)
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나로 치환
    new_id = re.sub('\.{2,}', '.', new_id)
    
    # 4단계: 마침표(.)가 처음이나 끝에 있다면 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이라면 "a"를 대입
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면 첫 15자만 남김
    new_id = new_id[:15]
    # 자르고 나서 끝에 마침표(.)가 있다면 제거
    new_id = new_id.rstrip('.')
    
    # 7단계: 길이가 2자 이하라면 마지막 문자를 반복해서 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
