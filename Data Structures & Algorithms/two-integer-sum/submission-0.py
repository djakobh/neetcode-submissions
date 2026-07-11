class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            new = target - n
            if new in map:
                return [map[new], i]
            map[n] = i
        return
