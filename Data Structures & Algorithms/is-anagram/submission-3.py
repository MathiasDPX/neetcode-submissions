class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = sorted(list(s))
        tChars = sorted(list(t))

        return tChars == sChars