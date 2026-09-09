class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        a = []
        for i in s:
            if i not in a:
                a.append(i)
            else:
                while a[0] != i:
                    a.pop(0)
                a.pop(0)
                a.append(i)                
            if c < len(a): c=len(a)
        return c
        