class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int L = 0;
        int R = numbers.length-1;

        while (L < R) {
            int sum = numbers[L] + numbers[R];
            if (sum == target) {
                return new int[] {L+1, R+1};
            } else if (sum > target) {
                R--;
            } else {
                L++;
            }
        }
        return new int[] {};
    }
}