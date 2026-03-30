class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackMap = {']':'[', '}':'{', ')':'('}
        for char in s:
            if char not in stackMap:
                stack.append(char)
            elif stack and stack[-1] == stackMap[char]:
                stack.pop() 
            else:
                return False

        return not stack