from collections import deque
def solution(order):
    answer = 0
    objective = deque(order[:])
    conveyer = deque()
    sub_con = []
    for i in range(len(order)):
        conveyer.append(i + 1)
        
    while objective:
        if conveyer and conveyer[0] == objective[0]:
            conveyer.popleft()
            objective.popleft()
            answer += 1
        elif sub_con and sub_con[-1] == objective[0]:
            sub_con.pop()
            objective.popleft()
            answer += 1
        elif conveyer:
            sub_con.append(conveyer.popleft())
        else:
            break
    return answer