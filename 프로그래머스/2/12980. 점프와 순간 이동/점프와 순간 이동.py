def solution(n):
    ans = 0
    new = n
    while new != 0:
        if new % 2 == 0:
            new = new // 2
        else:
            new = new - 1
            ans += 1
    
    return ans