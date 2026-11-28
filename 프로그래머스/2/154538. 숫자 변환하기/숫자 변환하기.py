from collections import deque
def solution(x, y, n):
    visited = [False] * (y + 1)
    visited[x] = True
    q = deque([(x, 0)])
    while q:
        num, trial = q.popleft()
        if num == y:
            return trial
        for dnum in (num, 2 * num, n):
            nnum = num + dnum
            if 0 <= nnum <= y and visited[nnum] == False:
                visited[nnum] = True
                q.append((nnum, trial + 1))
    
    return -1