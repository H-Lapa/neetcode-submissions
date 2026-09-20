class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = Counter(s)

        for char in t:
            if char in sCount:
                if sCount[char] == 1:
                    del sCount[char]
                else:
                    sCount[char] -= 1
            else:
                return False

        return not sCount