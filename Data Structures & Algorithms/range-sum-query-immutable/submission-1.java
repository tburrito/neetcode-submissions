class NumArray {

    int[] nums;

    public NumArray(int[] nums) {
        this.nums = nums;
    }
    
    public int sumRange(int left, int right) {
        int size = nums.length;
        int[] prefixSum = new int[size];

        prefixSum[0] = nums[0];

        for (int i = 1; i < size; i++){
            prefixSum[i] = nums[i] + prefixSum[i-1];
        }
        if (left - 1 < 0)
            return prefixSum[right];
        else
            return prefixSum[right] - prefixSum[left -1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */