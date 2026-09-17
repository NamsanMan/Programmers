def solution(k, score):
    answer = []
    honor = []
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
        elif len(honor) >= k:
            if score[i] > min(honor):
                honor.remove(min(honor))
                honor.append(score[i])

        answer.append(min(honor))
    return answer