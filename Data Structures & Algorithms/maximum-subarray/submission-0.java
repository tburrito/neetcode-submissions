class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currSum = 0;

        int size = nums.length;

        for (int i = 0; i < size; i++){
            currSum = Math.max(0, currSum) + nums[i];
            maxSum = Math.max(maxSum, currSum);
        }

        return maxSum;
    }
    
}
