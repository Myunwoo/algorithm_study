class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            if ss in ['(', '[', '{']:
                stack.append(ss)
                continue
            elif ss is ')':
                if not stack or stack[-1] is not '(':
                    return False
            elif ss is ']':
                if not stack or stack[-1] is not '[':
                    return False
            elif ss is '}':
                if not stack or stack[-1] is not '{':
                    return False
            stack.pop()
        
        if stack:
            return False
        return True
                    