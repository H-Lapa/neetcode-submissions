class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
        L, R = 0, len(nums)-1

        while L <= R:
            mid = L + ((R-L) // 2)
            # print(nums[mid], mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1

