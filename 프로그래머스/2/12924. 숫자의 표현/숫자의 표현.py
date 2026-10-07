def solution(n):
    answer = 0
    seq_num = []
    start_num = 1
    
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            seq_num.append(i)
    else:
        for i in range(1, n // 2 + 2):
            seq_num.append(i)

    while start_num < seq_num[-1]:
        summation = 0
        x = start_num
        while summation < n:
            summation += x
            x += 1
        if summation == n:
            answer += 1
        start_num += 1
    
    answer += 1
    return answer