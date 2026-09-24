"3550. Smallest Index With Digit Sum Equal to Index"
from typing import List
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx == sum(map(int, str(val))):
                return idx
        return -1