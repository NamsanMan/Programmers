from collections import deque

def solution(n, computers):
    answer = 1
    visited = [False] * n
    visited[0] = True
    i = 0
    while i < n:
        if visited[i] == True:
            q = deque([i])
            while q:
                x = q.popleft()
                for nx in range(n):
                    if computers[x][nx] == 1 and visited[nx] == False:
                        visited[nx] = True
                        q.append(nx)
            i += 1
        else:
            answer += 1
            visited[i] = True
            
    return answer