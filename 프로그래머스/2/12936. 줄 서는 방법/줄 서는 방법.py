def solution(n, k):
    answer = []
    ppl = []
    for i in range(1, n + 1):
        ppl.append(i)
    new_k = k - 1
    new_n = n - 1
    while new_n:
        div = 1
        for i in range(1, new_n + 1):
            div = div * i
        idx  = new_k // div
        new_k = new_k % div
        new_n -= 1
        answer.append(ppl.pop(idx))
        
    answer.append(ppl.pop())
    return answer