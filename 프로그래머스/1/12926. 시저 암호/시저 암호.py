def solution(s, n):
    answer = ''
    # a = 97, z = 122
    # A = 65, Z = 90
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            answer += (chr(((ord(s[i]) - 97) + n) % 26 + 97))
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            answer += (chr(((ord(s[i]) - 65) + n) % 26 + 65))
    return answer