def to_binary(n):
    remain = n
    bin_str = ""
    while remain != 0:
        bin_str = bin_str + str(remain % 2)
        remain = remain // 2
    bin_str = bin_str[::-1]
    
    return bin_str
        
def solution(s):
    answer = []
    answer.append(0)
    answer.append(0)
    before_0_removed = s[:]
    
    while before_0_removed != "1":
        after_0_removed = ""
        for i in range(len(before_0_removed)):
            if before_0_removed[i] == "1":
                after_0_removed += "1"
            else:
                answer[1] += 1
        before_0_removed = to_binary(len(after_0_removed))
        answer[0] += 1        
    
    return answer