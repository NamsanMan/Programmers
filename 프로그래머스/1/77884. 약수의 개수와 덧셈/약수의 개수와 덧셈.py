def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        count = 0
        for n in range(1, i):
            if i % n == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        elif count % 2 == 1:
            answer -= i
    return -(answer)