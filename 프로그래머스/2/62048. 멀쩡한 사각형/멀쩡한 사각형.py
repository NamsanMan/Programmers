def solution(w, h):
    a, b = w, h
    while b:
        a, b = b, a % b          # 유클리드 호제법, a = gcd(w, h)
    return w * h - (w + h - a)