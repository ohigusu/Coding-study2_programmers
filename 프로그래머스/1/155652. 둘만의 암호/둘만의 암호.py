def solution(s, skip, index):
    alpha_set = set(skip)  # skip을 집합으로 변환 (O(1) 조회 가능)
    alpha_list = [chr(i) for i in range(97, 123) if chr(i) not in alpha_set]  # 건너뛸 문자 제외

    alpha_dict = {char: i for i, char in enumerate(alpha_list)}  # 빠른 인덱스 조회를 위한 딕셔너리 생성
    alpha_len = len(alpha_list)  # 유효한 알파벳 개수 (매번 len() 호출 방지)

    return ''.join(alpha_list[(alpha_dict[char] + index) % alpha_len] for char in s)

#     answer = ''
#     alpha = 'abcdefghijklmnopqrstuvwxyz'

#     for sk in skip:
#         alpha = alpha.replace(sk,'')
#     for char in s:
#         idx = (alpha.index(char)+index)%len(alpha)
#         answer += alpha[idx]
#     return answer