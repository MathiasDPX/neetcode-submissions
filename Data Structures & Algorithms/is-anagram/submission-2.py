def count_chars(word):
    maps = {}
    for letter in word:
        maps[letter] = word.count(letter)

    return maps

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return count_chars(s) == count_chars(t)