class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        startIdx = 0
        answer = 0

        for i in range(len(s)):
            cur = s[i]
            # 겹치지 않음
            if cur not in dic:
                dic[cur] = i
                answer = max(answer, i-startIdx+1)
                continue
            
            # startIdx부터 dic[cur]까지는 중복 없는 부분 문자열로 사용불가
            temp = dic[cur]
            for j in range(startIdx, dic[cur]):
                del dic[s[j]]
            startIdx = temp + 1
            dic[cur] = i
            answer = max(answer, i-startIdx+1)

        return answer
# 처음 풀 때 이렇게 풀었음. 정답이 나오긴 하나, O(n^2)형태의 알고리즘

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        startIdx = 0
        answer = 0

        for i in range(len(s)):
            cur = s[i]
            # 중복이 발생했으며, 현재 내가 관리 중인 서브 스트링 이내임
            if cur in dic and dic[cur] >= startIdx:
                startIdx = dic[cur]+1
            dic[cur] = i
            answer = max(answer, i-startIdx+1)

        return answer
# 사실 dic를 비워줄 필요는 없음. 관심범위를 나타내는 startIdx만 움직여주면 된다.
