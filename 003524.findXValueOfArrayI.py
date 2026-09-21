"3524. Find X Value of Array I"
from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result=[0]*k
        dp=[0]*k
        n = len(nums)

        for num in nums:
            new_dp=[0]*k
            num_mod=num%k

            new_dp[num_mod]+=1
            for i in range(k):
                new_mod = (i * num_mod) % k
                new_dp[new_mod] += dp[i]
            for i in range(k):
                result[i] += new_dp[i]

            dp = new_dp

        return result