from collections import deque
def solution(bridge_length, weight, truck_weights):
    time,total_weight = 0,0
    bridge,truck_weights = deque(),deque(truck_weights)
    while truck_weights or bridge:
        time += 1
        if bridge and time-bridge[0][1]>=bridge_length:
            out_truck,_=bridge.popleft()
            total_weight -= out_truck
        
        if truck_weights and total_weight+truck_weights[0]<=weight:
            next_truck = truck_weights.popleft()
            bridge.append((next_truck,time))
            total_weight += next_truck
    return time
