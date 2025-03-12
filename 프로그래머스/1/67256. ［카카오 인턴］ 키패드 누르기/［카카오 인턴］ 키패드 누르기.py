def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표 설정
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 시작 위치
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    # 가운데 열 숫자
    middle_numbers = [2, 5, 8, 0]
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_pos = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_pos = keypad[number]
        else:
            # 가운데 열 -> 거리 계산
            target_pos = keypad[number]
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = target_pos
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = target_pos
            else:
                if hand == 'right':
                    answer += 'R'
                    right_pos = target_pos
                else:
                    answer += 'L'
                    left_pos = target_pos
    
    return answer
