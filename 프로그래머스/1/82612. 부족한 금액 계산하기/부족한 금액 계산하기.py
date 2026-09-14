def solution(price, money, count):
    answer = 0
    need = 0
    for i in range(1, count + 1):
        need  += i * price
    if need <= money:
        answer = 0
    elif need > money:
        answer = need  - money
    return answer