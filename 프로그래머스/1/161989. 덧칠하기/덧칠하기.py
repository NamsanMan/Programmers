def solution(n, m, section):
    answer = 0
    wall = []
    for i in range(1, n + 1):
        wall.append(1)
    
    for i in range(len(section)):
        wall[section[i] - 1] = 0
    
    for i in range(n):
        if wall[i] == 0:
            for j in range(i, min(i + m, n)):
                wall[j] = 1
            answer += 1
                
    

    return answer