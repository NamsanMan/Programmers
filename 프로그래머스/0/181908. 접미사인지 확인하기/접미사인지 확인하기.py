def solution(my_string, is_suffix):
    answer = 0
    list_str = []
    for i in range(len(my_string)):
        list_str.append(my_string[i:])
    if is_suffix in list_str:
        return 1
    else:
        return 0