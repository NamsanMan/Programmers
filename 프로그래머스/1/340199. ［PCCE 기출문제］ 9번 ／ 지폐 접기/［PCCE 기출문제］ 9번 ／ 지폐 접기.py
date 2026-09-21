def solution(wallet, bill):
    answer = 0
    w = wallet
    b = bill

    while not (max(b) <= max(w) and min(b) <= min(w)):
        b[b.index(max(b))] = max(b) // 2
        answer += 1

    return answer