from collections import deque
def solution(x, y, n):
    current = x
    visited = [False] * y
    visited[current - 1] = True
    q = deque([(current, 0)])
    while q:
        c, cnt = q.popleft()
        if c == y:
            return cnt
        
        n1 = c + n
        n2 = c * 2
        n3 = c * 3
        if n1 <= y and visited[n1 - 1] == False:
            visited[n1 - 1] = True
            q.append((n1, cnt + 1))
        if n2 <= y and visited[n2 - 1] == False:
            visited[n2 - 1] = True
            q.append((n2, cnt + 1))
        if n3 <= y and visited[n3 - 1] == False:
            visited[n3 - 1] = True
            q.append((n3, cnt + 1))
    
    return -1