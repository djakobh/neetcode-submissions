class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        alpha = {}

        for word in strs:
            sort = tuple(sorted(word))
            alpha.setdefault(sort, []).append(word)

        for value in alpha.values():
            output.append(value)

        return output