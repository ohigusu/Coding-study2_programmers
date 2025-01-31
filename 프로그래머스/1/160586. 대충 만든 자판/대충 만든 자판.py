# def solution(keymap, targets):
#     answer = []
#     book = {}
#     for key in keymap:
#         for idx,k in enumerate(key):
#             if k in book and idx >= book[k]:
#                 pass
#             else:
#                 book[k] = idx
                
#     n = len(targets)
#     for i in range(0,n):
#         store = []
#         for target in targets[i]:
#             if target in book:
#                 store.append(book[target])
#         if len(store) > 0:
#             answer.append(sum(store))
#         else:
#             answer.append(-1)
#     return answer
def solution(keymap, targets):
    book = {}

    # 최소 키 입력 횟수 저장
    for key in keymap:
        for idx, char in enumerate(key):
            book[char] = min(book.get(char, float('inf')), idx + 1)  # 1-based index

    # targets 처리
    result = []
    for target in targets:
        total_presses = 0
        for char in target:
            if char in book:
                total_presses += book[char]
            else:
                total_presses = -1
                break  # target을 작성할 수 없으므로 종료
        result.append(total_presses)

    return result
