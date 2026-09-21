def solution(n):
    is_prime = [True] * (n + 1)

    is_prime[0] = False
    is_prime[1] = False

    i = 2

    while i * i <= n:
        if is_prime[i] == True:
            j = i * i

            while j <= n:
                is_prime[j] = False
                j += i

        i += 1

    answer = 0

    for i in range(2, n + 1):
        if is_prime[i] == True:
            answer += 1

    return answer