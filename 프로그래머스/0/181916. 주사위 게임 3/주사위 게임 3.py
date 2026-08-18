def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    if dice[0] == dice[3]:
        return 1111 * dice[0]
    
    
    elif dice[0] == dice[2]:
        return (10 * dice[0] + dice[3]) ** 2
    elif dice[1] == dice[3]:
        return (10 * dice[1] + dice[0]) ** 2
    
    
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2])
    
    elif dice[0] == dice[1]:
        return dice[2] * dice[3]
    elif dice[1] == dice[2]:
        return dice[0] * dice[3]
    elif dice[2] == dice[3]:
        return dice[0] * dice[1]
    
    else:
        return dice[0]