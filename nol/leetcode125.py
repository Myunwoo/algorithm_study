class Solution:
    def isAlpha(self, s):
        o = ord(s)
        return (65 <= o <= 90) or (97 <= o <= 122)    
    def isNumeric(self, s):
        return 48 <= ord(s) <= 57

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:
            if not self.isAlpha(s[left]) and not self.isNumeric(s[left]):
                left += 1
                continue
            if not self.isAlpha(s[right]) and not self.isNumeric(s[right]):
                right -= 1
                continue
            
            if self.isAlpha(s[left]) and not self.isAlpha(s[right]):
                return False
            elif not self.isAlpha(s[left]) and self.isAlpha(s[right]):
                return False
            
            if self.isNumeric(s[left]):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
                continue
            
            if self.isAlpha(s[left]):
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                continue
        
        return True