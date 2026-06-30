class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n)[2:]).zfill(32)[::-1]

        return int(s, 2)