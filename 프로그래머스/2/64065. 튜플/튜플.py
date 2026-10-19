def solution(s):
    answer = []
    s_new = s[2:-2]
    temp = s_new.split("},{")
    tup = []
    for i in range(len(temp)):
        numbers = temp[i].split(',')
        tup.append(numbers)
    tup.sort(key = len)
    
    for i in range(len(tup)):
        numbers = set(tup[i])
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer