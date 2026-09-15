"2472. Maximum Number of Non-overlapping Palindrome Substrings"
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]

        dp = [0] * (n + 1)

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (
                    length <= 2 or pal[l + 1][r - 1]
                ):
                    pal[l][r] = True

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            for r in range(i + k - 1, n):
                if pal[i][r]:
                    dp[r + 1] = max(dp[r + 1], dp[i] + 1)

        return dp[n]