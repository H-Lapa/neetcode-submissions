class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            if num > 0:
                break

            L, R = i+1, len(nums)-1

            while L < R:
                if num + nums[L] + nums[R] == 0:
                    res.append([num, nums[L], nums[R]])
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    while L < R and nums[L] == nums[L+1]:
                        L += 1

                    L += 1
                    R -= 1
                elif num + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1

        return res


            