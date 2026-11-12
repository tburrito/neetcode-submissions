class Solution {
    public int pivotIndex(int[] nums) {
        int size = nums.length;
        int[] pivotSum = new int[size + 1];

        pivotSum[0] = 0;
        for (int i = 1; i <= size;i++){
            pivotSum[i] = pivotSum[i-1] + nums[i - 1];
        }

        for (int i = 0; i < size; i++){
            int leftSum = pivotSum[i];
            int rightSum = pivotSum[size] - pivotSum[i+1];

            if (leftSum == rightSum)
                return i;
        }

        return -1;
        
    }
}