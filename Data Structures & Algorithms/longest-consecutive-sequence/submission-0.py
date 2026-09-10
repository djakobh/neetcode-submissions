class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final = set(nums)
        longest = 0 
        
        for num in nums:
            if (num - 1) not in final:
                length = 0
                while (num + length) in final:
                    length += 1
                longest = max(length, longest)
        return longest
