def calculation(x, y, s):
    if s == '+':
        return x + y
    elif s == '-':
        return x - y
    elif s == '*':
        return x * y

def solution(expression):
    # 숫자와 연산자 분리 (기존 방식과 동일)
    tokens, num = [], ''
    for ch in expression:
        if ch in '+-*':
            tokens.append(int(num))
            tokens.append(ch)
            num = ''
        else:
            num += ch
    tokens.append(int(num))

    orders = [('*', '+', '-'), ('*', '-', '+'), ('+', '*', '-'),
              ('+', '-', '*'), ('-', '*', '+'), ('-', '+', '*')]
    best = 0
    for order in orders:
        t = tokens
        for op in order:                        # 우선순위가 높은 연산자부터
            stack = [t[0]]
            for i in range(1, len(t), 2):       # t[i] = 연산자, t[i+1] = 숫자
                if t[i] == op:
                    stack[-1] = calculation(stack[-1], t[i + 1], op)   # 직전 결과와 바로 계산
                else:
                    stack.append(t[i])
                    stack.append(t[i + 1])
            t = stack
        best = max(best, abs(t[0]))
    return best