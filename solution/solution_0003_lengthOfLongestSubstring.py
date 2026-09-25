class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        length_of_longest_substring = 1
        left, right = 0, 0
        gained = set(s[0])

        while right + 1 < len(s):
            right += 1
            if s[right] in gained:
                while left < right and s[left] != s[right]:
                    gained.remove(s[left])
                    left += 1
                left += 1
            else:
                gained.add(s[right])
                length_of_longest_substring = max(length_of_longest_substring, right-left+1)
        return length_of_longest_substring

if __name__ == '__main__':
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))
