def solution(numbers, hand):
    answer = ""

    position = {
        "left": [3, 0],   # *
        "right": [3, 2]   # #
    }

    mapping = {
        "1": [0, 0], "2": [0, 1], "3": [0, 2],
        "4": [1, 0], "5": [1, 1], "6": [1, 2],
        "7": [2, 0], "8": [2, 1], "9": [2, 2],
        "0": [3, 1]
    }

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            position["left"] = mapping[str(n)]
            answer += "L"

        elif n == 3 or n == 6 or n == 9:
            position["right"] = mapping[str(n)]
            answer += "R"

        else:
            left_distance = (
                abs(position["left"][0] - mapping[str(n)][0])
                + abs(position["left"][1] - mapping[str(n)][1])
            )

            right_distance = (
                abs(position["right"][0] - mapping[str(n)][0])
                + abs(position["right"][1] - mapping[str(n)][1])
            )

            if left_distance < right_distance:
                position["left"] = mapping[str(n)]
                answer += "L"

            elif left_distance > right_distance:
                position["right"] = mapping[str(n)]
                answer += "R"

            else:
                if hand == "left":
                    position["left"] = mapping[str(n)]
                    answer += "L"
                else:
                    position["right"] = mapping[str(n)]
                    answer += "R"

    return answer