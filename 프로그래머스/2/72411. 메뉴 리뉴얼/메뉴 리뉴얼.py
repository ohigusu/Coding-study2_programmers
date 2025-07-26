from itertools import combinations
from collections import Counter
def solution(orders, course):
    # 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
    # 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
    # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
    '''
    입력:
        1) orders: 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열
        2) course: 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열
    출력: "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열 (사전 순으로 오름차순 정렬)
    '''
    answer = []

    for c in course:
        combs = []
        for order in orders:
            order = sorted(order)  # 알파벳 순 정렬
            combs += combinations(order, c)  # 조합 생성

        counter = Counter(combs)

        if not counter:
            continue
        
        max_count = max(counter.values())
        if max_count < 2:
            continue

        for comb, cnt in counter.items():
            if cnt == max_count:
                answer.append(''.join(comb))  

    return sorted(answer)