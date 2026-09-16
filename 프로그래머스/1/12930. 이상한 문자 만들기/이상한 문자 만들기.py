def solution(s):
    answer = ''
    arr_s = s.split(" ")

    for i in range(len(arr_s)):
        arr_s[i] = list(arr_s[i])

        for x in range(len(arr_s[i])):
            if x % 2 == 0:
                arr_s[i][x] = arr_s[i][x].upper()
            else:
                arr_s[i][x] = arr_s[i][x].lower()

        arr_s[i] = "".join(arr_s[i])

    answer = " ".join(arr_s)

    return answer