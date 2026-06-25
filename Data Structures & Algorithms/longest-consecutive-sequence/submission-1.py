class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]-1:
                return False

        return True

    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        # Remove duplicates
        nums = list(set(nums))

        # Order the list
        nums = sorted(nums)

        startingPoints = [idx for idx in range(len(nums)) if (nums[idx-1] < nums[idx] - 1) or idx==0]
        startingPoints.append(len(nums) + 1)

        subsuites = [nums[startingPoints[i]:startingPoints[i+1]] for i in range(len(startingPoints)-1)]

        return max(len(lst) for lst in subsuites)