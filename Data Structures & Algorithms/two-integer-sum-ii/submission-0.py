class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        while L < R:
            ptrSum = numbers[L] + numbers[R]

            if ptrSum == target:
                return [L+1, R+1]
            elif ptrSum > target:
                R -= 1
            else:
                L += 1

        