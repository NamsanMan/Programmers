def solution(friends, gifts):
    answer = []
    given = {}
    recived = {}
    gift_points = []

    for i in range(len(gifts)):
        row = gifts[i].split(" ")

        if row[0] not in given:
            given[row[0]] = []

        given[row[0]].append(row[1])

    for i in range(len(gifts)):
        row = gifts[i].split(" ")

        if row[1] not in recived:
            recived[row[1]] = []

        recived[row[1]].append(row[0])

    g_point = []
    r_point = []

    for i in range(len(friends)):
        if friends[i] not in given:
            g_point.append(0)
        else:
            g_point.append(len(given[friends[i]]))

        if friends[i] not in recived:
            r_point.append(0)
        else:
            r_point.append(len(recived[friends[i]]))

    for i in range(len(friends)):
        gift_points.append(g_point[i] - r_point[i])

    for i in range(len(friends)):
        answer.append(0)

    # 친구 두 명씩 비교
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            give_i_to_j = 0
            give_j_to_i = 0

            if friends[i] in given:
                give_i_to_j = given[friends[i]].count(friends[j])

            if friends[j] in given:
                give_j_to_i = given[friends[j]].count(friends[i])

            if give_i_to_j > give_j_to_i:
                answer[i] += 1

            elif give_i_to_j < give_j_to_i:
                answer[j] += 1

            else:
                if gift_points[i] > gift_points[j]:
                    answer[i] += 1

                elif gift_points[i] < gift_points[j]:
                    answer[j] += 1

    return max(answer)