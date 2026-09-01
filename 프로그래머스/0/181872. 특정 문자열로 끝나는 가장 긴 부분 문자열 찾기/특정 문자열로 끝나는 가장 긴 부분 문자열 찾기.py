def solution(myString, pat):
    end = myString.rfind(pat) + len(pat)
    return myString[:end]