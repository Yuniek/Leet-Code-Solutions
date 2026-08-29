from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1+nums2
        c.sort()
        if len(c)%2==1:
            r = c[(len(c)//2)]
        else:
            x = c[(len(c)//2)-1]
            y = c[(len(c)//2)]
            r = (x+y)/2
        return(r)
