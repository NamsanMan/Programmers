from collections import deque
def solution(rows, columns, queries):
    answer = []
    queue = deque(queries)
    maps = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(columns * i + j + 1)
        maps.append(row)
    while queue:
        y1, x1, y2, x2 = queue.popleft()
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        q_num = deque()     # 임시 저장할 번호
        smallest_num = 0    # 가장 작은 번호
        for c in range(x1, x2 + 1):
            if c == x1:
                smallest_num = maps[y1][c]
                q_num.append(maps[y1][c])
                maps[y1][c] = maps[y1 + 1][c]
            else:
                if smallest_num > maps[y1][c]:
                    smallest_num = maps[y1][c]
                q_num.append(maps[y1][c])
                maps[y1][c] = q_num.popleft()
        for r in range(y1 + 1, y2 + 1):
            if smallest_num > maps[r][x2]:
                smallest_num = maps[r][x2]
            q_num.append(maps[r][x2])
            maps[r][x2] = q_num.popleft()
        for c in range(x2 - 1, x1 - 1, -1):
            if smallest_num > maps[y2][c]:
                smallest_num = maps[y2][c]
            q_num.append(maps[y2][c])
            maps[y2][c] = q_num.popleft()
        for r in range(y2 - 1, y1,  -1):
            if smallest_num > maps[r][x1]:
                smallest_num = maps[r][x1]
            q_num.append(maps[r][x1])
            maps[r][x1] = q_num.popleft()
        answer.append(smallest_num)

    return answer