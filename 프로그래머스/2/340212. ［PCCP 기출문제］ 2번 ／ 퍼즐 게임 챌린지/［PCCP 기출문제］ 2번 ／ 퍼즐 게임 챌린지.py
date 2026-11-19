def solution(diffs, times, limit):
    level = 1
    until = max(diffs)
    lo, hi = 1, until                                   # 추가: 이분 탐색 범위

    while lo < hi:                                      # 변경: while 1 → 이분 탐색
        level = (lo + hi) // 2                          # 추가: 가운데 레벨 시도
        t = 0
        level_up_flag = False
        for i in range(len(diffs)):
            if diffs[i] <= level:
                t += times[i]
            else:
                t += (diffs[i] - level) * (times[i] + times[i - 1])   # 변경: replay 반복 → 곱셈
                t += times[i]
            if t > limit:                               # 변경: 더한 뒤 검사
                level_up_flag = True
                break
        if level_up_flag:
            lo = level + 1                              # 변경: 이 레벨로는 부족 → 위쪽 절반
        else:
            hi = level                                  # 변경: 이 레벨로 가능 → 아래쪽 절반

    return lo                                           # 변경: level → lo