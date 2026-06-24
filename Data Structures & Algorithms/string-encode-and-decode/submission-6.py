from json import loads, dumps

class Solution:

    def encode(self, strs: List[str]) -> str:
        return dumps(strs)

    def decode(self, s: str) -> List[str]:
        return loads(s)