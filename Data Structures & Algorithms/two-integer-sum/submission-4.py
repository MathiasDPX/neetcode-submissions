class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, i in enumerate(nums):
            for y, j in enumerate(nums, start=x):
                if i+j == target and x != y-x:
                    return [x,y-x]

        return []