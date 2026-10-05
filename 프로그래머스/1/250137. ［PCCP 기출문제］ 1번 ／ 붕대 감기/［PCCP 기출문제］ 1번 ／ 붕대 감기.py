def solution(bandage, health, attacks):
    answer = 0
    current_health = health
    
    attack_timing = []
    time_count = 0
    for i in range(len(attacks)):
        attack_timing.append(attacks[i][0])
    
    for time in range(attack_timing[0], attack_timing[-1] + 1):
        if time in attack_timing:
            current_health = current_health - attacks[attack_timing.index(time)][1]
            time_count = 0
            
        if current_health <= 0:
            return -1
            break
        else:
            if time not in attack_timing:
                if current_health < health:
                    current_health += bandage[1]
                    time_count += 1
                    if time_count == bandage[0]:
                        current_health += bandage[2]
                        time_count = 0
                    if current_health >= health:
                        current_health = health
        if time == attack_timing[-1]:
            return current_health
            