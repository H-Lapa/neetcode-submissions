class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # target-num : index of num

        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]

            hashmap[target-num] = i

        