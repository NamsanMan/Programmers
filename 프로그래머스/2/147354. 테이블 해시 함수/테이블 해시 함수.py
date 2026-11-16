def solution(data, col, row_begin, row_end):
    answer = 0
    data_new = sorted(data, key = lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        s = sum(v % i for v in data_new[i - 1])
        answer ^= s

    return answer