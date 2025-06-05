import math

def solution(fees, records):
    """
    fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    records: ["HH:MM 차량번호 IN/OUT", ...]
    return: 차량 번호 오름차순대로 계산된 주차 요금 리스트
    """
    # 1) 요금 기준
    base_time, base_fee, unit_time, unit_fee = fees

    # 2) 입차 시각을 분 단위로 저장할 딕셔너리
    in_time = {}      # { "0000": 360, "5961": 334, ... } 같은 구조

    # 3) 차량별 누적 주차 시간을 분 단위로 저장할 딕셔너리
    total_time = {}   # { "0000": 334, "0148": 670, "5961": 146, ... }

    # --- 1. 모든 기록을 차례대로 순회하며 IN/OUT 처리 ---
    for rec in records:
        time_str, car_num, action = rec.split()
        hh, mm = map(int, time_str.split(":"))
        cur_min = hh * 60 + mm   # 시각을 “분” 단위로 변환

        if action == "IN":
            # 입차: 차량번호 → 입차 시각(분) 저장
            in_time[car_num] = cur_min
        else:  # action == "OUT"
            # 출차: 딕셔너리에서 입차 시각을 꺼내고,
            # 출차 시각 − 입차 시각을 계산해 누적
            start = in_time.pop(car_num)  # pop 하면 in_time에서 제거됨
            duration = cur_min - start
            total_time[car_num] = total_time.get(car_num, 0) + duration

    # --- 2. 아직 출차 기록이 없는 차량(자동으로 23:59 출차 처리) ---
    end_of_day = 23 * 60 + 59  # 23:59를 분 단위로 환산하면 1439
    for car_num, start in in_time.items():
        duration = end_of_day - start
        total_time[car_num] = total_time.get(car_num, 0) + duration

    # --- 3. 차량 번호 오름차순으로 누적 시간에 따른 요금 계산 ---
    answer = []
    for car_num in sorted(total_time.keys()):
        t = total_time[car_num]  # 이 차량의 누적 주차 시간(분)
        if t <= base_time:
            fee = base_fee
        else:
            extra = t - base_time
            # (초과 시간 / 단위 시간)을 올림 처리
            count = math.ceil(extra / unit_time)
            fee = base_fee + count * unit_fee
        answer.append(fee)

    return answer
