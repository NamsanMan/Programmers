from collections import deque
def solution(board):
    H, W = len(board), len(board[0])
    for r in range(H):
        for c in range(W):
            if board[r][c] == "R":
                start = (r, c)
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        r, c = q.popleft()
        if board[r][c] == "G":
            return dist[r][c]
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r, c
            while 0 <= nr + dr < H and 0 <= nc + dc < W and board[nr + dr][nc + dc] != "D":
                nr += dr
                nc += dc
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return -1