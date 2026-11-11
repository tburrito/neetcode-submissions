class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;

        int[] output = new int[size];

        output[0] = 1;
        for (int i = 1; i < size; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }

        int suffix = 1;
        for (int i = size - 1; i >= 0; i--) {
            output[i] *= suffix;
            suffix *= nums[i];
        }

        return output;
    }
}