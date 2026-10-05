def solution(mats, park):
    height = len(park)
    width = len(park[0])

    dp = [[0] * width for _ in range(height)]
    max_size = 0

    for i in range(height):
        for j in range(width):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1

                if dp[i][j] > max_size:
                    max_size = dp[i][j]

    answer = -1

    for mat in mats:
        if mat <= max_size and mat > answer:
            answer = mat

    return answer