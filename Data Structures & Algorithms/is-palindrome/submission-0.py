class Solution:
    def isPalindrome(self, s: str) -> bool:
        #preprocess the string 
        newStr = ''

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        L, R = 0, len(newStr)-1

        while L < R:
            if newStr[L] != newStr[R]:
                return False
            
            L += 1
            R -= 1

        return True