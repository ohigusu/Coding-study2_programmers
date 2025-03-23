from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()  # (무게, 진입시간)
    total_weight = 0
    truck_weights = deque(truck_weights)
    while truck_weights or bridge:
        time += 1
        # 1. 다리에서 나갈 트럭 처리
        if bridge and time - bridge[0][1] >= bridge_length:
            out_truck, _ = bridge.popleft()
            total_weight -= out_truck

        # 2. 다리에 새 트럭 추가 가능하면 추가
        if truck_weights and total_weight + truck_weights[0] <= weight:
            next_truck = truck_weights.popleft()
            bridge.append((next_truck, time))
            total_weight += next_truck

    return time
