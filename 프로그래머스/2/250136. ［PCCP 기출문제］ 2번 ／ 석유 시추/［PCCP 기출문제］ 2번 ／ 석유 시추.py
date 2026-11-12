from collections import deque
def solution(land):
    H, W = len(land), len(land[0])
    visited = [[False] * W for _ in range(H)]
    col_sum = [0] * W
    for j in range(W):
        for i in range(H):
            if visited[i][j] == False and land[i][j] == 1:
                start = (i, j)
                visited[start[0]][start[1]] = True
                group = 1
                cols = {j}
                q = deque([start])
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and land[nr][nc] == 1 and visited[nr][nc] == False:
                            group += 1
                            visited[nr][nc] = True
                            cols.add(nc)
                            q.append((nr, nc))
                for c in cols:
                    col_sum[c] += group

    return max(col_sum)