def solution(my_string):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        answer.append(my_string.count(char))

    return answer