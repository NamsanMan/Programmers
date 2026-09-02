def solution(myStr):
    answer = []
    text_a = myStr.replace("a", " ")
    text_b = text_a.replace("b", " ")
    text_c = text_b.replace("c", " ")
    answer = text_c.split()
    if answer == []:
        return ["EMPTY"]
    return answer