def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if (i + 1) % 2 == 0:
            even += num_list[i]
        elif (i + 1) % 2 != 0:
            odd += num_list[i]
    if even > odd:
        return even
    elif even < odd:
        return odd
    else:
        return even