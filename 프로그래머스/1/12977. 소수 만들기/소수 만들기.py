def is_prime(n):
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                summation = nums[i] + nums[j] + nums[k]

                if is_prime(summation):
                    answer += 1

    return answer