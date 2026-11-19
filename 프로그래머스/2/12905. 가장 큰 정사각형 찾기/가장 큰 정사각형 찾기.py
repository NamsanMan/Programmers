def solution(board):
    answer = 0
    H = len(board)
    W = len(board[0])
    dp = [row[:] for row in board]
    best = 0
    for i in range(H):
        for j in range(W):
            if i > 0 and j > 0 and board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            best = max(best, dp[i][j])
    return best * best