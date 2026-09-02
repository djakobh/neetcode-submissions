class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        alpha = {}
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            alpha.setdefault(key, []).append(word)
            
        for value in alpha.values():
            output.append(value)
            
        return output