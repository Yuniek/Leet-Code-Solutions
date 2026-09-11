"16. 3Sum Closest"
from typing import List
class Solution:
    def threeSumClosest(self, nums:List[int], target: int) -> int:
        nums.sort()

        smallest_sum = sum(nums[:3])
        if smallest_sum >= target:
            return smallest_sum
        
        largest_sum = sum(nums[-3:])
        if largest_sum <= target:
            return largest_sum
        
        closest = smallest_sum
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if abs(total - target)<abs(closest - target):closest=total
                if total < target:
                    left+=1
                elif total > target:
                    right-=1
                elif total == target:
                    return total
        return closest