class Solution:
    def countOccurences(self, word:str) -> Dict[str, int]:
        maps = {}
        for letter in word:
            maps[letter] = word.count(letter)

        return maps

    def isAnagram(self, a:str, b:str) -> bool:
        return self.countOccurences(a) == self.countOccurences(b)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())