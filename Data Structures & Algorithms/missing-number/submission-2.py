class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n * (n + 1) // 2 # Sum of the range [0;n]
        
        return target - sum(nums)