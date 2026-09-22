def solution(keymap, targets):
    answer = []

    for i in range(len(targets)):
        number = 0
        possible = True

        for j in range(len(targets[i])):
            all_possible_numbers = []

            for a in range(len(keymap)):
                if targets[i][j] in keymap[a]:
                    for b in range(len(keymap[a])):
                        if keymap[a][b] == targets[i][j]:
                            all_possible_numbers.append(b + 1)

            if len(all_possible_numbers) == 0:
                possible = False
                break

            number += min(all_possible_numbers)

        if possible == True:
            answer.append(number)
        else:
            answer.append(-1)

    return answer