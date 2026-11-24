from collections import deque
def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x: x[1])
    n_plans = []
    for i in range(len(plans)):
        row = [plans[i][0], int(plans[i][1].split(":")[0]) * 60 + int(plans[i][1].split(":")[1]), int(plans[i][2])]
        n_plans.append(row)

    queue = deque(n_plans)
    subject = queue[0][0]
    left_time = queue[0][2]

    current_time = queue[0][1]
    queue.popleft()
    stack = []
    stack.append([subject, left_time])
    while queue or stack:
        if not stack:
            subject2, start2, duration2 = queue.popleft()
            stack.append([subject2, duration2])
            current_time = start2
            continue
        sub1, duration1 = stack.pop()
        if queue:
            start2 = queue[0][1]
            if current_time + duration1 <= start2:
                answer.append(sub1)
                current_time = current_time + duration1
            else:
                stack.append([sub1, current_time + duration1 - start2])
                subject2, start2, duration2 = queue.popleft()
                stack.append([subject2, duration2])
                current_time = start2
        else:
            answer.append(sub1)
    
    return answer