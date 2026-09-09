"3876. Construct Uniform Parity Array II"
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x & 1:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        return min_odd == float('inf') or min_odd < min_even