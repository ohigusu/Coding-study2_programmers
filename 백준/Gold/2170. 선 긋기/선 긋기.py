import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    li = []
    for i in range(1, 2 * N, 2):
        x = int(data[i])
        y = int(data[i + 1])
        li.append((x, y))
    
    li.sort()
    pre_x, pre_y = li[0]
    result = 0

    for x, y in li[1:]:
        if x <= pre_y:
            pre_y = max(pre_y, y)
        else:
            result += pre_y - pre_x
            pre_x, pre_y = x, y
    
    result += pre_y - pre_x
    print(result)

if __name__ == "__main__":
    main()