class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        number = {}
        number['I'] = 1
        number['V'] = 5
        number['X'] = 10
        number['L'] = 50
        number['C'] = 100
        number['D'] = 500
        number['M'] = 1000

        rule = {}
        rule['IV'] = 4
        rule['IX'] = 9
        rule['XL'] = 40
        rule['XC'] = 90
        rule['CD'] = 400
        rule['CM'] = 900

        i = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i] + s[i+1] in rule:
                    answer += rule[s[i] + s[i+1]]
                    i += 2
                else:
                    answer += number[s[i]]
                    i += 1
            else:
                answer += number[s[i]]
                i += 1

        return answer