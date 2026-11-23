from collections import deque
def solution(storage, requests):
    answer = 0
    # -1(외부)로 둘러싸인 array를 만들면서 각 알파벳의 시작 개수를 저장
    # 외부가 아닌 빈 공간은 0으로 표현
    left_overs = {}
    H, W = len(storage), len(storage[0])
    n_st = []
    for i in range(H):
        row = []
        if i == 0:
            for j in range(W + 2):
                row.append(-1)
            n_st.append(row)
            row = []
        for j in range(W):
            if j == 0:
                row.append(-1)
            row.append(storage[i][j])
            if storage[i][j] not in left_overs:
                left_overs[storage[i][j]] = 1
            else:
                left_overs[storage[i][j]] += 1
            if j == W - 1:
                row.append(-1)
        n_st.append(row)
        row = []
        if i == H - 1:
            for j in range(W + 2):
                row.append(-1)
            n_st.append(row)
    
    for req in requests:
        mode = len(req)
        if mode == 1 and req[0] in left_overs:
            for r in range(1, len(n_st) - 1):
                for c in range(1, len(n_st[0]) - 1):
                    if n_st[r][c] == req[0]:
                        flag = False
                        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if n_st[nr][nc] == -1:
                                n_st[r][c] = 0
                                flag = True
                        if flag:
                            left_overs[req[0]] -= 1
        elif mode == 2 and req[0] in left_overs:
            for r in range(1, len(n_st) - 1):
                for c in range(1, len(n_st[0]) - 1):
                    if n_st[r][c] == req[0]:
                        n_st[r][c] = 0
                        left_overs[req[0]] -= 1
        # 0을 -1로 갱신
        visited = [[False] * len(n_st[0]) for _ in range(len(n_st))]
        visited[0][0] = True
        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(n_st) and 0 <= nc < len(n_st[0]) and not visited[nr][nc] and (n_st[nr][nc] == -1 or n_st[nr][nc] == 0):
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    n_st[nr][nc] = -1
    
    for v in left_overs.values():
        answer += v
    return answer