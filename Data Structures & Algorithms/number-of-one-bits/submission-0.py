class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in range(n.bit_length()) if n & (1 << i)])