def solution(n):
    answer = 0
    available = [[0] * n for _ in range(n)]

    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for c in range(n):
            if available[row][c] == 0:
                # 밑줄 체크 밑 대각선 체크
                for h in range(row, n):
                    d = h - row
                    available[h][c] += 1
                    # 대각선
                    if c + d < n:
                        available[h][c + d] += 1
                    if c - d >= 0:
                        available[h][c - d] += 1
                dfs(row + 1)
                for h in range(row, n):
                    d = h - row
                    available[h][c] -= 1
                    # 대각선
                    if c + d < n:
                        available[h][c + d] -= 1
                    if c - d >= 0:
                        available[h][c - d] -= 1
    
    dfs(0)
    return answer