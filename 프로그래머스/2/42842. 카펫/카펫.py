from math import sqrt
def solution(brown, yellow):

    whole_tile = brown + yellow
    b = 1
    while b <= int(sqrt(whole_tile)):
        if whole_tile % b == 0:
            a = whole_tile // b
            if brown == 2 * a + 2 * (b - 2) and yellow == (a - 2) * (b - 2):
                return [a, b]
        
        b += 1
