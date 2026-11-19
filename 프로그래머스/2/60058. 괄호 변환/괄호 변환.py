from collections import deque
def is_right(s):
    stack = []
    queue = deque()
    for i in range(len(s)):
        queue.append(s[i])
    while queue:
        if stack and queue[0] == ')' and stack[-1] == '(':
            stack.pop()
            queue.popleft()
        else:
            stack.append(queue.popleft())
    if stack:
        return False
    else:
        return True
    
def solution(p):    
    def into_right(new_p):
        if not new_p:
            return ''
        u = ''
        v = ''
        count_left = 0
        count_right = 0
        for i in range(len(new_p)):
            if new_p[i] == '(':
                count_left += 1
            elif new_p[i] == ')':
                count_right += 1
            if count_left == count_right:
                u = new_p[:i + 1]
                v = new_p[i + 1:]
                break
        if is_right(u):
            return u + into_right(v)
        else:
            flipped = ''
            for ch in u[1:-1]:
                if ch == '(':
                    flipped += ')'
                else:
                    flipped += '('
            return '(' + into_right(v) + ')' + flipped

    return into_right(p)