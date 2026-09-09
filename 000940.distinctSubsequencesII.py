"940. Distinct Subsequences II"
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        last = {}
        m = 0

        for ch in s:
            old = last.get(ch, 0)

            new = m + 1

            m = m + new - old

            last[ch] = new

        return m % MOD


print(Solution().distinctSubseqII("aaa"))