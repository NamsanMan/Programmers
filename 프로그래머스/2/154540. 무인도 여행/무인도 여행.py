from collections import deque
def solution(maps):
    answer = []
    H, W = len(maps), len(maps[0])
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if maps[i][j] != 'X' and visited[i][j] == False:
                start = (i, j)
                visited[i][j] = True
                q = deque([start])
                total = int(maps[i][j])
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != 'X' and visited[nr][nc] == False:
                            visited[nr][nc] = True
                            total += int(maps[nr][nc])
                            q.append((nr, nc))
                answer.append(total)
    
    if not answer:
        return [-1]
    else:
        return sorted(answer)