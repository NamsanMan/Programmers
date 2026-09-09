def solution(n):
    answer = ''
    str_n = str(n)
    lst = []
    
    for i in str_n:
        lst.append(i)
    lst.sort(reverse=True)
    
    for i in lst:
        answer += i
    
    return int(answer)