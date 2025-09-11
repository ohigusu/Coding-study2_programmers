#from collections import Counter
def solution(participant, completion):
    hash_map = {}
    # 완주자 명단 카운팅
    for com in completion:
        if com in hash_map:
            hash_map[com] += 1
        else:
            hash_map[com] = 1
     # 참가자 명단 확인
    for part in participant:
        if part not in hash_map or hash_map[part] == 0:
            return part
        else:
            hash_map[part] -= 1
            