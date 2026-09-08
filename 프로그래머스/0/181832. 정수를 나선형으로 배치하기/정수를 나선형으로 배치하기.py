def solution(n):
    answer = [[0] * n for _ in range(n)]

    def assign(y, x, num, size):
        if size <= 0:
            return

        answer[y][x] = num

        directions = [
            (0, 1, size - 1),   # 오른쪽
            (1, 0, size - 1),   # 아래
            (0, -1, size - 1),  # 왼쪽
            (-1, 0, size - 2)   # 위
        ]

        for dy, dx, count in directions:
            for _ in range(count):
                y += dy
                x += dx
                num += 1
                answer[y][x] = num

        assign(y, x + 1, num + 1, size - 2)

    assign(0, 0, 1, n)
    return answer