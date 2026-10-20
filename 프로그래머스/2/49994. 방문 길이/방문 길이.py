def solution(dirs):
    answer = 0
    position_history = [[0, 0]]
    dx = [0, 0, -1, 1]      # up, down, left, right
    dy = [1, -1, 0, 0]
    for directory in dirs:
        x = position_history[-1][0]
        y = position_history[-1][1]
        
        if directory == "U":
            next_x = x + dx[0]
            next_y = y + dy[0]
        elif directory == "D":
            next_x = x + dx[1]
            next_y = y + dy[1]
        elif directory == "L":
            next_x = x + dx[2]
            next_y = y + dy[2]
        elif directory == "R":
            next_x = x + dx[3]
            next_y = y + dy[3]
        if next_x < -5 or next_x > 5:
            continue
        if next_y < -5 or next_y > 5:
            continue
        
        is_first = True
        for history_check in range(1, len(position_history)):
            before = position_history[history_check - 1]
            after = position_history[history_check]
            if before == [x, y] and after == [next_x, next_y]:
                is_first = False
                break
            if before == [next_x, next_y] and after == [x, y]:
                is_first = False
                break
        
        if is_first == True:
            answer += 1
            position_history.append([next_x, next_y])
        else:
            position_history.append([next_x, next_y])
    
    return answer