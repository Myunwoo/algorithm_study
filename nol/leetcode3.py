class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 문자가 마지막으로 등장한 위치를 저장할 딕셔너리
        char_index = {}

        # 현재 부분 문자열의 시작 위치 (왼쪽 포인터)
        left = 0

        # 가장 긴 부분 문자열의 길이를 저장할 변수
        max_len = 0

        # 문자열의 각 문자를 오른쪽 포인터(right)로 순회
        for right in range(len(s)):
            current_char = s[right]

            # 만약 현재 문자가 이미 등장했고,
            # 그 인덱스가 현재 윈도우(left ~ right) 안에 있다면,
            # 중복이므로 왼쪽 포인터를 그 다음 위치로 이동시켜야 한다.
            if current_char in char_index and char_index[current_char] >= left:
                # 중복된 문자를 피하기 위해 left를 해당 위치 다음으로 이동
                left = char_index[current_char] + 1

            # 현재 문자의 인덱스를 딕셔너리에 기록 (항상 갱신)
            char_index[current_char] = right

            # 현재 윈도우의 길이를 계산하고, 최댓값 갱신
            window_length = right - left + 1
            max_len = max(max_len, window_length)

        # 결과 반환
        return max_len