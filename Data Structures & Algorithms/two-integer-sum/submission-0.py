class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            a = nums[i]
            for j in range(len(nums)):
                if i == j: continue
                b = nums[j]
                #if a == b: continue
                if a+b == target:
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)

        return result