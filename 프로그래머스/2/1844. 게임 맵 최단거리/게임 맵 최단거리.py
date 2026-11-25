from collections import deque
def solution(maps):
    answer = 0
    H, W = len(maps), len(maps[0])
    dist = [[0] * W for _ in range(H)]
    start = (0, 0)
    dist[0][0] = 1
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    
    if dist[H - 1][W - 1] == 0:
        return -1
    else:
        return dist[H - 1][W - 1]