class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        return encoded.join(string + "dylan" for string in strs)


    def decode(self, s: str) -> List[str]:
        strings = s.split("dylan")
        strings.pop()
        return strings
