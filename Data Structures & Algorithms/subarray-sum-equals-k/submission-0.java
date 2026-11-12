class Solution {
    public int subarraySum(int[] nums, int k) {
        int prefixSum = 0;
        Map<Integer, Integer> found = new HashMap<>();
        int count = 0;

        found.put(0,1);

        for (int i = 0; i < nums.length; i++){
            prefixSum += nums[i];
            if(found.containsKey(prefixSum - k)){
                count += found.get(prefixSum-k);
            }
            
            if(found.containsKey(prefixSum))
                found.put(prefixSum, found.get(prefixSum) + 1);
            else
                found.put(prefixSum, 1);

        }

        return count;
    }
}