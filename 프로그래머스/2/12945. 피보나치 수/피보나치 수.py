from collections import deque

def solution(n):
    answer = 0
    queue = deque([0, 1])
    x = 1
    
    while x != n:
        nxt = queue[-1] + queue[-2]
        queue.popleft()
        queue.append(nxt)
        x += 1
    
    return queue[-1] % 1234567