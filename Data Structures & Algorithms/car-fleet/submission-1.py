class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair and sort cars by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            # 2. Calculate independent time to target
            time_to_target = (target - pos) / spd
            
            # 3. If stack is empty, or this car takes LONGER than the fleet ahead,
            # it cannot catch up. It forms its own new fleet.
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
                
            # If time_to_target <= stack[-1], it catches up to the fleet ahead.
            # We do nothing (it merges into the existing fleet on top of the stack).
            
        # 4. The number of remaining elements in the stack is the number of fleets
        return len(stack)
