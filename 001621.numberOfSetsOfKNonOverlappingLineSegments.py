"1621. Number of Sets of K Non-Overlapping Line Segments"
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k+1):
            running_sum = 0
            for i in range(1, n):
                running_sum += dp[i - 1][j - 1]
                print(running_sum)

        print(dp)
        return 0