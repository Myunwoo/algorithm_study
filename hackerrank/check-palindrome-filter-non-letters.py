def isAlpha(x):
    ordVal = ord(x)
    return (ord('a') <= ordVal <= ord('z')) or (ord('A') <= ordVal <= ord('Z'))

def isAlphabeticPalindrome(code):
    left, right = 0, len(code) - 1
    
    while left < right:
        lVal, rVal = code[left], code[right]
        if not isAlpha(lVal):
            left += 1
        elif not isAlpha(rVal):
            right -= 1
        elif lVal.lower() == rVal.lower():
            left += 1
            right -= 1
        else:
            return 0
    return 1