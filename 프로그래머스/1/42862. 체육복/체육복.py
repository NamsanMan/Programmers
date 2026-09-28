def solution(n, lost, reserve):
    answer = 0
    latest_lost = lost[:]
    latest_reserve = reserve[:]

    # 도난 + 여벌 학생은 자기 체육복만 사용함
    for i in lost:
        if i in latest_reserve:
            latest_lost.remove(i)
            latest_reserve.remove(i)

    for i in range(1, n + 1):
        if i in latest_lost:
            if i - 1 in latest_reserve:
                latest_reserve.remove(i - 1)
                answer += 1

            elif i + 1 in latest_reserve:
                latest_reserve.remove(i + 1)
                answer += 1

        else:
            answer += 1

    return answer