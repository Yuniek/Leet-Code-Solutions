"3414. Maximum Score of Non-overlapping Intervals"

from typing import List
from bisect import bisect_right
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])

        starts = [x[0] for x in arr]

        nxt = [
            bisect_right(starts, arr[i][1])
            for i in range(n)
        ]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, original_idx = arr[i]

            for k in range(1, 5):
                best_score, best_ids = dp[i + 1][k]

                next_score, next_ids = dp[nxt[i]][k - 1]

                take_score = w + next_score
                take_ids = tuple(sorted((original_idx,) + next_ids))

                if (take_score > best_score or
                    (take_score == best_score and take_ids < best_ids)):
                    dp[i][k] = (take_score, take_ids)
                else:
                    dp[i][k] = (best_score, best_ids)

        return list(dp[0][4][1])