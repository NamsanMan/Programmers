from collections import deque
def solution(land):
    column = [0] * len(land[0])
    H, W = len(land), len(land[0])
    visited = [[False] * W for _ in range(H)]
    for j in range(W):
        for i in range(H):
            if land[i][j] == 1 and visited[i][j] == False:
                start = (i, j)
                visited[i][j] = True
                column_records = [j]
                total = 1
                q = deque([start])
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == False and land[nr][nc] == 1:
                            total += 1
                            visited[nr][nc] = True
                            if nc not in column_records:
                                column_records.append(nc)
                            q.append((nr, nc))
                for c in column_records:
                    column[c] += total
    
    
    return max(column)