class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = []

        for x in nums:
            if x in existing:
                return True
            else:
                existing.append(x);
        
        return False