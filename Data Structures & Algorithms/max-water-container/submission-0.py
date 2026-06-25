class Solution:
    def getBucketSize(self, i, j):
        # j is always greater than i
        w = j - i
        h = min(self.heights[i], self.heights[j])
        return w * h

    def maxArea(self, heights: List[int]) -> int:
        self.heights = heights

        biggestSize = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i >= j:
                    continue
                    
                currSize = self.getBucketSize(i, j)

                if currSize > biggestSize:
                    biggestSize = currSize

        return biggestSize
