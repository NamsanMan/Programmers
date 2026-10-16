def solution(topping):
    answer = 0
    
    younger = {}
    for item in topping:
        if item not in younger:
            younger[item] = 0
        younger[item] += 1
        
    older = set()
    for i in range(len(topping) - 1):
        item = topping[i]
        
        younger[item] -= 1
        if younger[item] == 0:
            younger.pop(item)
        older.add(item)
        
        if len(younger) == len(older):
            answer += 1
    return answer