def solution(n):
    answer = 0
    next_n = n + 1
    count = 0
    count_next = 0
    n_bin = bin(n)[2:]
    
    for i in n_bin:
        if i == "1":
            count += 1
    
    while count != count_next:
        count_next = 0
        for i in bin(next_n)[2:]:
            if i == "1":
                count_next += 1
        next_n += 1
    
    print(bin(n)[2:])
    print(next_n)
    return next_n - 1