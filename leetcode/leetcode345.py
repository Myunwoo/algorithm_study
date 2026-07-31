class Solution:
    def reverseVowels(self, s: str) -> str:
        sArr = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        idxStck = []
        valStck = []

        for i in range(len(sArr)):
            if sArr[i] in vowels:
                idxStck.append(i)
                valStck.append(sArr[i])
        
        i = 0
        while valStck:
            curVal = valStck.pop()
            sArr[idxStck[i]] = curVal
            i += 1
        
        return ''.join(sArr)