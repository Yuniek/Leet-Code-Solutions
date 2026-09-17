"1477. Find Two Non-overlapping Sub-arrays Each With Target Sum"
from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)

        # best[i] = shortest target-sum subarray
        # completely inside arr[0:i]
        best = [float("inf")] * (n + 1)

        left = 0
        current_sum = 0
        answer = float("inf")

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                # Is there a previous non-overlapping subarray?
                if best[left] != float("inf"):
                    answer = min(answer, length + best[left])

                # Record this subarray as the best one ending here.
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == float("inf") else answer