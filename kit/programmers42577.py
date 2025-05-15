def solution(phone_book): 
    hashMap = {}
    
    for p in phone_book:
        hashMap[p] = True
    
    for nums in hashMap:
        word = ''
        for num in nums:
            word += num
            
            if word in hashMap and word != nums:
                return False
    
    return True