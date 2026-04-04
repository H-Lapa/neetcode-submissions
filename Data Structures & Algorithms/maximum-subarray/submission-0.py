class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = -10000
        cumNum = 0
        for num in nums:
            cumNum = max(cumNum+num, num)
            maxNum = max(maxNum, cumNum)

        return maxNum