# Definition for singly-linked list.
from typing import Optional, List, Any

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def linkedListToList(ln: ListNode | Any, l=None):
            if ln.next is None:
                return [ln.val]

            if l is None:
                l = [ln.val]

            l += linkedListToList(ln.next)
            return l

        l = linkedListToList(head)

        if len(l) < 3:
            return [-1, -1]

        left, mid, right, idx = l[0], l[1], l[2], 2

        critical_point_idx = []

        while True:

            if (left < mid and mid > right) or (left > mid and mid < right):
                critical_point_idx.append(idx - 1)

            if idx + 1 >= len(l):
                break

            idx = idx + 1

            left = l[idx - 2]
            mid = l[idx - 1]
            right = l[idx]

        if len(critical_point_idx) < 2:
            return [-1, -1]

        min_distance = float("inf")

        for i in range(1, len(critical_point_idx)):
            distance = critical_point_idx[i] - critical_point_idx[i - 1]

            if distance < min_distance:
                min_distance = distance

        max_distance = critical_point_idx[-1] - critical_point_idx[0]

        return [min_distance, max_distance]