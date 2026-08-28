def solution(arr):
    answer = 0

    while True:
        a = []

        for i in arr:
            if i >= 50 and i % 2 == 0:
                a.append(i // 2)

            elif i < 50 and i % 2 == 1:
                a.append(i * 2 + 1)

            else:
                a.append(i)

        if a == arr:
            return answer

        arr = a
        answer += 1