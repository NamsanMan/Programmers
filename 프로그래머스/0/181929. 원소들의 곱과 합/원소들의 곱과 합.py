def solution(num_list):
    answer = 0
    mul = 1
    sumation = 0
    for i in range(len(num_list)):
        mul = mul * num_list[i]
        sumation += num_list[i]
    
    if mul < sumation**2:
        answer = 1
    elif mul > sumation**2:
        answer = 0
        
        
    return answer