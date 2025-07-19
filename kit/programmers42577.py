# 전화번호 배열이 주어질 때
# 특정 전화번호가 다른 전화번호의 접두어일 때 False를 반환해라
# 그렇지 않다면 True를 반환해라

# phone_book 길이 : 1~ㅌㅌㅌ
# 타입은? 문자열
# 중복이 발생? 

def solution(phone_book): 
    phoneMap = {}
    
    # O(n)
    # phone_book
    # hashMap > phone
    for phone in phone_book:
        phoneMap[phone] = True
    
    # O(n)
    # hashMap key
    # k phone
    for key in phoneMap:
        for i in range(len(key)-1):
            if key[0:i+1] in phoneMap:
                return False    
    
    return True