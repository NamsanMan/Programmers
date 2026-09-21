def solution(babbling):
    answer = 0

    for word in babbling:
        before = ""
        can_say = True

        while word != "":
            if word[:3] == "aya":
                now = "aya"
                word = word[3:]

            elif word[:2] == "ye":
                now = "ye"
                word = word[2:]

            elif word[:3] == "woo":
                now = "woo"
                word = word[3:]

            elif word[:2] == "ma":
                now = "ma"
                word = word[2:]

            else:
                can_say = False
                break

            if now == before:
                can_say = False
                break

            before = now

        if can_say == True:
            answer += 1

    return answer