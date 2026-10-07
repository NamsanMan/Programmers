def solution(s):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s_list = s.split(" ")

    for i in range(len(s_list)):
        s_list[i] = s_list[i].lower()

    for i in range(len(s_list)):
        if s_list[i] != "" and s_list[i][0] in alphabet:
            s_list[i] = s_list[i][0].upper() + s_list[i][1:]

    answer = " ".join(s_list)

    return answer