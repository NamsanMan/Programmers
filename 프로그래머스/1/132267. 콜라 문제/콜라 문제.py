def solution(a, b, n):
    answer = 0
    r = n
    
    while r > a - 1:
    
        if r % a == 0:
            answer += (r // a) * b
            r = (r // a) * b
        elif r % a != 0:
            answer += (r // a) * b
            r = (r // a) * b + r % a
            
    return answer