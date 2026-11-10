def solution(players, m, k):
    answer = 0
    number_of_server = [1] * 24
    for t in range(24):
        if players[t] < number_of_server[t] * m:
            continue
        else:
            how_many_add = ((players[t] - number_of_server[t] * m) // m) + 1
            if t + k > 24:
                for i in range(t, 24):
                    number_of_server[i] += how_many_add
            else:
                for i in range(t, t + k):
                    number_of_server[i] += how_many_add
            answer += how_many_add
    return answer