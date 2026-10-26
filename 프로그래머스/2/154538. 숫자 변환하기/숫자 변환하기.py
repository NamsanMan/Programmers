from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = [False] * (y + 1)
    visited[x] = True
    while queue:
        current_num, calculations = queue.popleft()
        if current_num == y:
            return calculations
        plus = current_num + n
        times2 = current_num * 2
        times3 = current_num * 3

        if plus <= y and visited[plus] == False:
            visited[plus] = True
            queue.append((plus, calculations + 1))
            
        
        if times2 <= y and visited[times2] == False:
            visited[times2] = True
            queue.append((times2, calculations + 1))
            
            
        if times3 <= y and visited[times3] == False:
            visited[times3] = True
            queue.append((times3, calculations + 1))
    
    return -1