def solution(lottos, win_nums):
    answer = []
    correct = 0
    new_lottos = lottos[:]
    new_win_nums = win_nums[:]

    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                correct += 1
                new_lottos.remove(lottos[i])
                new_win_nums.remove(lottos[i])
    
    if correct >= 2:
        rank = 7 - correct
    else:
        rank = 6
        
    answer.append(rank)
    
    for i in range(len(new_lottos)):
        if new_lottos[i] == 0:
            correct += 1
            
    
        
    if correct >= 2:
        rank = 7 - correct
    else:
        rank = 6
        
    answer.append(rank)

    return answer[::-1]