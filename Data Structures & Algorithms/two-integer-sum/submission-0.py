class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        size = len(nums)

        while (i < size - 1):
            if nums[i] + nums[j] == target:
                return list([i,j])
            else:
                j += 1
            
            if j == size:
                i += 1
                j = i + 1
        
        return [-1,-1]