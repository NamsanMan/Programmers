def solution(phone_book):
    set_pb = set(phone_book)
    
    for phone in set_pb:
        prefix = ''
        
        for i in range(len(phone) - 1):
            prefix += phone[i]
            
            if prefix in set_pb:
                return False
            
    
    return True