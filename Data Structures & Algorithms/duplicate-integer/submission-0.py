class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nnums = nums.copy()
            del nnums[i]
            if nums[i] in nnums:
                return True
        return False