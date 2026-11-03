def solution(storey):
    answer = 0
    check = storey
    while check:
        number = check % 10
        if number < 5:
            answer += number
            check = check // 10
        elif number > 5:
            answer += 10 - number
            check = check // 10 + 1
        else:
            answer += number
            check = check // 10
            if check % 10 > 4:
                check += 1
            else:
                continue
    return answer