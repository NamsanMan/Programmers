def transformer(input_n, to_k):
    number = input_n
    output = ''
    while number:
        output += str(number % to_k)
        number = number // to_k
    output = output[::-1]
    return output

def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    converted = transformer(n, k)
    zero_filter = []
    row = ''
    for i in range(len(converted)):
        if converted[i] != '0':
            row += converted[i]
        elif converted[i] == '0':
            if row:
                zero_filter.append(row)
                row = ''
    if row:
        zero_filter.append(row)

    for i in range(len(zero_filter)):
        if is_prime(int(zero_filter[i])):
            answer += 1
    return answer