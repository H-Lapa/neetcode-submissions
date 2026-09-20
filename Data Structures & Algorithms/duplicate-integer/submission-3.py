class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracked = set()
        for num in nums:
            if num in tracked:
                return True
            tracked.add(num)

        return False

        