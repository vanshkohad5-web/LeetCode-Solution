class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # char -> last seen index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If we've seen this character and it's within the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len