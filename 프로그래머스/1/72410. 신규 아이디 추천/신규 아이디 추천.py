def solution(new_id):
    id_check = new_id[:]
    id_check = id_check.lower()
    
    id_check_2 = ''
    id_check_3 = ''
    
    valid_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "."]
    
    for i in id_check:
        if i in valid_list:
            id_check_2 += i
    
    count_dot = 0
    for i in id_check_2:
        if i == ".":
            count_dot += 1
        if i != ".":
            if count_dot >= 1:
                id_check_3 += "."
                id_check_3 += i
                count_dot = 0
            else:
                id_check_3 += i
                count_dot = 0
                
    if id_check_3.startswith("."):
        if id_check_3.endswith("."):
            id_check_3 = id_check_3[1 : -1]
        else:
            id_check_3 = id_check_3[1 :]
    if id_check_3.endswith("."):
        id_check_3 = id_check_3[: -1]
    
    if id_check_3 == "":
        id_check_3 += "a"
    
    if len(id_check_3) >= 16:
        id_check_3 = id_check_3[: 15]
        if id_check_3.endswith("."):
            id_check_3 = id_check_3[:-1]
        
    if len(id_check_3) <= 2:
        while len(id_check_3) < 3:
            id_check_3 += id_check_3[-1]
    
    

    return id_check_3