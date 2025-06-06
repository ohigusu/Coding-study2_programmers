def split_filename(fname):
    """
    파일명 fname을 HEAD, NUMBER, TAIL로 수작업 분리하여 반환한다.
    - HEAD: 첫 번째 숫자가 나오기 전까지의 문자 (최소 1자)
    - NUMBER: 숫자가 연속된 최대 5글자(또는 숫자가 끝날 때까지)
    - TAIL: 나머지
    """
    n = len(fname)
    head = ""
    number = ""
    i = 0
    
    # 1) HEAD 추출: 숫자(digit)가 처음 나올 때까지
    while i < n and not fname[i].isdigit():
        head += fname[i]
        i += 1

    # 2) NUMBER 추출: 숫자가 연속된 1~5글자 (숫자가 끝나거나 5글자 채우면 중단)
    #    (문제 조건상 반드시 숫자가 하나 이상 존재하므로, head 이후에 곧바로 숫자가 온다고 가정)
    cnt = 0
    while i < n and fname[i].isdigit() and cnt < 5:
        number += fname[i]
        i += 1
        cnt += 1

    # 3) 나머지를 TAIL로 둠 (정렬에는 사용하지 않음)
    tail = fname[i:]
    
    return head, number, tail


def solution(files):
    # stable sort를 이용하므로, 키가 같으면 원래 입력 순서가 유지된다.
    def sort_key(fname):
        head, number, tail = split_filename(fname)
        # HEAD 비교는 대소문자 구분 없이 → 모두 소문자로 바꿔서 비교
        # NUMBER 비교는 앞의 0을 무시한 “정수값”으로 비교
        return (head.lower(), int(number))
    
    return sorted(files, key=sort_key)