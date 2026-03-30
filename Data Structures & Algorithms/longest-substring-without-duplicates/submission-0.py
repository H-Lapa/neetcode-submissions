class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()

        L = 0
        maxLen = 0

        for R in range(len(s)):
            if s[R] in visited:
                while s[L] != s[R]:
                    visited.remove(s[L])
                    L += 1
                L += 1
            else:
                visited.add(s[R])


            maxLen = max(maxLen, R-L+1)

        return maxLen
