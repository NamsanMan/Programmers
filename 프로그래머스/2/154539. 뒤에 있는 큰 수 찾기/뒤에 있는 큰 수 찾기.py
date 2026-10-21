def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[i] > stack[-1][0]:
            value = numbers[i]
            index = stack[-1][1]
            answer[index] = value
            stack.pop()
        stack.append([numbers[i], i])
    while stack:
        index = stack[-1][1]
        answer[index] = -1
        stack.pop()
    return answer