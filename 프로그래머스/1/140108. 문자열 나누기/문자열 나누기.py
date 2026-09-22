def solution(s):
    answer = 0
    index = 0

    while index < len(s):
        x = s[index]
        count_self = 0
        count_another = 0
        divide = False

        for i in range(index, len(s)):
            if s[i] == x:
                count_self += 1
            else:
                count_another += 1

            if count_self == count_another:
                answer += 1
                index = i + 1
                divide = True
                break

        if divide == False:
            answer += 1
            break

    return answer