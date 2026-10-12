def solution(n,a,b):
    answer = 0
    new_a_num = a
    new_b_num = b
    
    if new_a_num < new_b_num:
        while new_a_num != new_b_num:
            if new_a_num % 2 == 0:
                new_a_num = new_a_num // 2
            elif new_a_num % 2 == 1:
                new_a_num = (new_a_num + 1) // 2
            if new_b_num % 2 == 0:
                new_b_num = new_b_num // 2
            elif new_b_num % 2 == 1:
                new_b_num = (new_b_num + 1) // 2
            answer += 1
    
        
    elif new_a_num > new_b_num:
        while new_a_num != new_b_num:
            if new_a_num % 2 == 0:
                new_a_num = new_a_num // 2
            elif new_a_num % 2 == 1:
                new_a_num = (new_a_num + 1) // 2
            if new_b_num % 2 == 0:
                new_b_num = new_b_num // 2
            elif new_b_num % 2 == 1:
                new_b_num = (new_b_num + 1) // 2
            answer += 1
    return answer