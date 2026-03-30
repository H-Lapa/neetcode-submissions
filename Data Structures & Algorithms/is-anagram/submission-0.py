class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #counter function
        sCount = {}
        for char in s:
            if char in sCount:
                sCount[char] += 1
            else:
                sCount[char] = 1

        for char in t:
            if char in sCount:
                sCount[char] -= 1

                if sCount[char] == 0:
                    del sCount[char]

            else:
                return False

        return not sCount