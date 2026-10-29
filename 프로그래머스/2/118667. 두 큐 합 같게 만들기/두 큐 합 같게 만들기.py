from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    total = sum(q1) + sum(q2)

    if total % 2 != 0:
        return -1

    half = total // 2
    sum_q1 = sum(q1)  # 한 번만 계산

    # 두 큐의 길이가 각각 n일 때 최대 3n번 이동
    limit = len(queue1) * 3

    while answer <= limit:
        if sum_q1 == half:
            return answer

        if sum_q1 < half:
            if not q2:
                break
            point = q2.popleft()
            q1.append(point)
            sum_q1 += point
        else:
            if not q1:
                break
            point = q1.popleft()
            q2.append(point)
            sum_q1 -= point

        answer += 1

    return -1