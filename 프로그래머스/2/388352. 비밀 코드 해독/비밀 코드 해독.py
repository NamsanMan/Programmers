def solution(n, q, ans):
    answer = 0
    candidates = []
    current = []
    def dfs(start):
        if len(current) == 5:
            candidates.append(current[:])
            return
        for i in range(start, n + 1):
            current.append(i)
            dfs(i + 1)
            current.pop()
    dfs(1)
    
    for check in candidates:
        continue_flag = False
        for i in range(len(q)):
            cnt = 0
            for j in range(len(q[i])):
                if q[i][j] in check:
                    cnt += 1
            if cnt != ans[i]:
                continue_flag = True
                break
        if continue_flag:
            continue
        else:
            answer += 1
    
    return answer