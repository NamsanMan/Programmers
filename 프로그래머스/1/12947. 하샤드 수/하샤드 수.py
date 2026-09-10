def solution(x):
    string = str(x)
    a = 0
    b = 0
    for i in range(len(string)):
        a = int(string[i])
        b += a
    if x % b == 0:
        return True
    else:
        return False