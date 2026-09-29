def solution(wallpaper):
    answer = []
    file_pos = []
    lux = 0
    luy = 0
    rdx = 0
    rdy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            row = []
            if wallpaper[i][j] == "#":
                row.append(i)
                row.append(j)
                file_pos.append(row)
    lux = min(file_pos, key = lambda row : row[0])[0]
    luy = min(file_pos, key = lambda row : row[1])[1]
    rdx = max(file_pos, key = lambda row : row[0])[0] + 1
    rdy = max(file_pos, key = lambda row : row[1])[1] + 1
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    return answer