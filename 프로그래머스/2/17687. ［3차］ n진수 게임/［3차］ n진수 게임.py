def encode(into_n, input_n):
    if input_n == 0:
        return '0'
    calculate = input_n
    encoded = ''
    while calculate:
        if calculate % into_n == 10:
            encoded += 'A'
        elif calculate % into_n == 11:
            encoded += 'B'
        elif calculate % into_n == 12:
            encoded += 'C'
        elif calculate % into_n == 13:
            encoded += 'D'
        elif calculate % into_n == 14:
            encoded += 'E'
        elif calculate % into_n == 15:
            encoded += 'F'
        else:
            encoded += str(calculate % into_n)
        calculate = calculate // into_n
    return encoded[::-1]
def solution(n, t, m, p):
    answer = ''
    sequence = ''
    number = 0
    while len(answer) < t:
        if len(sequence) <= (p - 1) + len(answer) * m:
            sequence += encode(n, number)
            number += 1
        else:
            answer += sequence[(p - 1) + len(answer) * m]
    return answer