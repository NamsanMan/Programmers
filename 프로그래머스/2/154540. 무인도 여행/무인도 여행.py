from collections import deque
def solution(maps):
    answer = []
    H, W = len(maps), len(maps[0])
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if maps[i][j] != "X" and not visited[i][j]:
                visited[i][j] = True
                total = int(maps[i][j])
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != "X" and not visited[nr][nc]:
                            total += int(maps[nr][nc])
                            visited[nr][nc] = True
                            q.append((nr, nc))
                answer.append(total)
    return sorted(answer) if answer else [-1]