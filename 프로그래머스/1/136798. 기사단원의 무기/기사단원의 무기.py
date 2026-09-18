def num_yaksu(n):
    num = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                num += 1
            else:
                num += 2

        i += 1

    return num


def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        count = num_yaksu(i)

        if count <= limit:
            answer += count
        else:
            answer += power

    return answer