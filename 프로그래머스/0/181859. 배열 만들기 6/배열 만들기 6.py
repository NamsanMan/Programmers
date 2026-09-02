def solution(arr):
    stk = []
    for i in range(len(arr)):
        if i < len(arr):
            if stk == []:
                stk.append(arr[i])
            elif stk[-1] == arr[i]:
                stk.pop()
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
    if stk == []:
        return [-1]
    return stk