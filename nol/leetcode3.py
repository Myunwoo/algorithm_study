class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}  # Dictionary to store the most recent occurrence of each character
        max_len = 0
        start = 0
    
        for end in range(len(s)):
            if s[end] in char_dict:
                # If the current character is already in the dictionary,
                # update the start pointer to the next index of the repeating character
                start = max(start, char_dict[s[end]] + 1)
    
            char_dict[s[end]] = end  # Update the most recent occurrence of the character
            max_len = max(max_len, end - start + 1)
    
        return max_len