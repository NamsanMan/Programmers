def solution(s):
    answer = 0
    answer = s
    if answer.startswith("+"):
        return int(answer[1:])
    elif answer.startswith("-"):
        return int(answer)
    else:
        return int(answer)