def solution(n, m):
    answer = []
    a = 0
    b = 0
    if n <= m:
        for i in range(1, n + 1):
            if n % i == 0:
                if m % i == 0:
                    a = i
        
    elif m < n:
        for i in range(1, m + 1):
            if m % i == 0:
                if n % i == 0:
                    a = i
    # 최소공배수 공식
    b = n * m // a
    answer.append(a)
    answer.append(b)
    return answer