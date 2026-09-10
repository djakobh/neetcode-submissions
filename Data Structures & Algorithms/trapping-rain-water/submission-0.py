class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]
        total = 0 

        while l < r:
            if maxleft < maxright:
                l += 1 
                maxleft = max(maxleft, height[l])
                total += maxleft - height[l]
            else:
                r -= 1 
                maxright = max(maxright, height[r])
                total += maxright - height[r]
                
        return total 