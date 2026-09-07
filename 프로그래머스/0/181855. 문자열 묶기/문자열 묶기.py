def solution(strArr):
    count = {}

    for word in strArr:
        length = len(word)

        if length in count:
            count[length] += 1
        else:
            count[length] = 1

    return max(count.values())