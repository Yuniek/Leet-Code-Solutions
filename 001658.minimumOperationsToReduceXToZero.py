"1658. Minimum Operations to Reduce X to Zero"
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target_sum = sum(nums)-x

        if target_sum<0:
            return -1

        if target_sum == 0:
            return n

        ans = -1
        current_sum = 0
        left=0
        for right, val in enumerate(nums):
            current_sum += val
            while current_sum > target_sum:
                current_sum -= nums[left]
                left+=1
            if current_sum == target_sum:
                ans = max(ans, (right-left+1))
        return n-ans if ans != -1 else -1