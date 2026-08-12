def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if code[idx] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if idx % 2 == 0 and mode == 0:
                ret += code[idx]
            elif idx %2 == 1 and mode == 1:
                ret += code[idx]
    if ret == "":
        return "EMPTY"
        
    return ret