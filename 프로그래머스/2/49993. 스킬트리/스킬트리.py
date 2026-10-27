from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        queue = deque(skill)
        available_flag = True
        for skills in skill_trees[i]:
            if skills in queue and skills == queue[0]:
                queue.popleft()
            elif skills in queue and skills != queue[0]:
                available_flag = False
                continue
        if available_flag == True:
            answer += 1
    
    return answer