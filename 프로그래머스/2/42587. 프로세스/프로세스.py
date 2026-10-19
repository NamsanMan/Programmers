from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        row = []
        row.append(priorities[i])
        if i == location:
            row.append(True)
        else:
            row.append(False)
        queue.append(row)
    
    while queue:
        now = queue.popleft()
        higher_exists = False
        for next_node in queue:
            if now[0] < next_node[0]:
                higher_exists = True
                break
        if higher_exists:
            queue.append(now)
        else:
            answer += 1
            if now[1] == True:
                return answer
                
    
    print(queue)
    return answer