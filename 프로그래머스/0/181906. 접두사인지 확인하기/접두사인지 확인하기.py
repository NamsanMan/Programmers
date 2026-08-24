def solution(my_string, is_prefix):

    temp = []
    for i in range(len(my_string)):
        temp.append(my_string[:i+1])
        
    if is_prefix in temp:
        return 1
    else:
        return 0