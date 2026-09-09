def solution(n):
    answer = 0
    str_n = str(n)
    
    for i in str_n:
        int_n = int(i)
        
        answer += int_n

    return answer