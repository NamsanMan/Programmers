from collections import deque
def solution(places):
    answer = []
    for room in range(len(places)):
        class_room = places[room]
        next_room_flag = False
        for H in range(5):
            for W in range(5):
                if places[room][H][W] == 'P':
                    start = (H, W)
                    dist = [[-1] * 5 for _ in range(5)]
                    dist[start[0]][start[1]] = 0
                    q = deque([start])
                    while q:
                        r, c = q.popleft()
                        if dist[r][c] == 2:
                            continue
                        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < 5 and 0 <= nc < 5 and dist[nr][nc] == -1 and class_room[nr][nc] == 'O':
                                dist[nr][nc] = dist[r][c] + 1
                                q.append((nr, nc))
                            if 0 <= nr < 5 and 0 <= nc < 5 and dist[nr][nc] == -1 and class_room[nr][nc] == 'P':
                                dist[nr][nc] = dist[r][c] + 1
                                q.append((nr, nc))
                    for r in range(5):
                        for c in range(5):
                            if not (r, c) == start and class_room[r][c] == 'P' and 0 < dist[r][c] < 3:
                                answer.append(0)
                                next_room_flag = True
                                break
                        if next_room_flag == True:
                            break
                    if next_room_flag == True:
                        break
            if next_room_flag == True:
                break
        if next_room_flag == False:
            answer.append(1)
    return answer