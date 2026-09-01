def solution(myString):
    answer = []

    parts = myString.split("x")

    for word in parts:
        if word != "":
            answer.append(word)

    answer.sort()

    return answer