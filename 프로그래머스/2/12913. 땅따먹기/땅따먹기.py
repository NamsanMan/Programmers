def solution(land):
    row = land[0]

    for i in range(1, len(land)):
        new_row = []

        for j in range(4):
            best = max(row[:j] + row[j + 1:])

            new_row.append(land[i][j] + best)

        row = new_row

    return max(row)