def solution(str1, str2):
    lower_str1 = str1.lower()
    lower_str2 = str2.lower()
    A = []
    B = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(lower_str1) - 1):
        if lower_str1[i] in alphabet and lower_str1[i+1] in alphabet:
            duo = lower_str1[i] + lower_str1[i+1]
            A.append(duo)
    for i in range(len(lower_str2) - 1):
        if lower_str2[i] in alphabet and lower_str2[i+1] in alphabet:
            duo = lower_str2[i] + lower_str2[i+1]
            B.append(duo)
    
    if A == [] and B == []:
        return 65536
    A_and_B = []
    if_used = [False] * len(B)
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j] and if_used[j] == False:
                A_and_B.append(A[i])
                if_used[j] = True
                break
    
    A_or_B = []
    for i in range(len(A)):
        A_or_B.append(A[i])
    for i in range(len(B)):
        A_or_B.append(B[i])
    for i in range(len(A_and_B)):
        A_or_B.remove(A_and_B[i])

    return int((len(A_and_B) / len(A_or_B)) * 65536)