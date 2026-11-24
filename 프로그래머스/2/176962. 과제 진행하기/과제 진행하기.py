def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x: x[1])
    state = {}
    for i in range(len(plans)):
        state[plans[i][0]] = [int(plans[i][1].split(":")[0]) * 60 + int(plans[i][1].split(":")[1]), int(plans[i][2])]
    print(state)
    stack = []
    for t in range(0, 24 * 60):
        for name in state:
            if state[name][0] == t:
                stack.append([name, state[name][1]])
        if stack:
            stack[-1][1] -= 1
            if stack[-1][-1] == 0:
                answer.append(stack.pop()[0])
    while stack:
        answer.append(stack.pop()[0])
    
    return answer