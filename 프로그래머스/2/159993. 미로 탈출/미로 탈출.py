from collections import deque
def solution(maps):
    answer = 0
    H, W = len(maps), len(maps[0])
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
    dist_to_lever = [[-1] * W for _ in range(H)]
    dist_to_lever[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != "X" and dist_to_lever[nr][nc] == -1:
                dist_to_lever[nr][nc] = dist_to_lever[r][c] + 1
                queue.append((nr, nc))
    if dist_to_lever[lever[0]][lever[1]] == -1:
        return -1
    else:
        answer += dist_to_lever[lever[0]][lever[1]]
    
    dist_to_end = [[-1] * W for _ in range(H)]
    dist_to_end[lever[0]][lever[1]] = 0
    queue = deque([lever])
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != "X" and dist_to_end[nr][nc] == -1:
                dist_to_end[nr][nc] = dist_to_end[r][c] + 1
                queue.append((nr, nc))
    if dist_to_end[end[0]][end[1]] == -1:
        return -1
    else:
        answer += dist_to_end[end[0]][end[1]]
        return answer