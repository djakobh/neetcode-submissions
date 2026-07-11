class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDupe = set(nums)

        if len(hasDupe) == len(nums):
            return False
        else:
            return True