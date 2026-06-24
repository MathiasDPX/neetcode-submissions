class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        
        for num in nums:
            occurences[num] = nums.count(num)

        topk = sorted(occurences, key=occurences.get, reverse=True)

        return topk[:k]