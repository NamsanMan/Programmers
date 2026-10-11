from collections import deque
def solution(n):
    answer = 0
    row = deque([])
    for i in range(1, n + 1):
        if i < 3:
            row.append(i)
        else:
            row.append(row[0] + row[1])
            row.popleft()
    answer = row[-1] % 1234567
    return answer