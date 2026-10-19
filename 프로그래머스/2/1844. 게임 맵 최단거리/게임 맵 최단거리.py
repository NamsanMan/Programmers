from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append([0, 0, 1])
    
    visited = []
    for i in range(n):
        row = [False] * m
        visited.append(row)
        
    visited[0][0] = True
    
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]
    
    while queue:
        h, w, count = queue.popleft()
        
        if h == n - 1 and w == m - 1:
            return count
        
        for i in range(4):
            next_h = h + dh[i]
            next_w = w + dw[i]
            
            if next_h < 0 or next_h >= n:
                continue
            if next_w < 0 or next_w >= m:
                continue
            if maps[next_h][next_w] == 0:
                continue
            if visited[next_h][next_w] == True:
                continue
                
            visited[next_h][next_w] = True
            queue.append([next_h, next_w, count + 1])
        
    return -1