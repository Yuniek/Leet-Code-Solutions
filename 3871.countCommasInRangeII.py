"3871. Count Commas in Range II"
class Solution:
    def countCommas(self, n: int) -> int:
        a = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)
            a += (end - start + 1) * commas

            start *= 1000
            commas += 1

        return a