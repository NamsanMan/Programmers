def solution(dartResult):
    scores = []
    index = 0

    while index < len(dartResult):
        # 숫자
        if dartResult[index:index + 2] == "10":
            score = 10
            index += 2
        else:
            score = int(dartResult[index])
            index += 1

        # S, D, T
        if dartResult[index] == "S":
            score = score
        elif dartResult[index] == "D":
            score = score ** 2
        else:  # T
            score = score ** 3

        index += 1

        # *, #는 있으면 처리
        if index < len(dartResult):
            if dartResult[index] == "*":
                score *= 2

                if len(scores) > 0:
                    scores[-1] *= 2

                index += 1

            elif dartResult[index] == "#":
                score *= -1
                index += 1

        scores.append(score)

    return sum(scores)