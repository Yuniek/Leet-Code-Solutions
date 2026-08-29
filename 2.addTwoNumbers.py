import typing as t
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToLinkedList(List:list):
    if len(List) == 1: return ListNode(List[0])
    return ListNode(List[0], ListToLinkedList(List[1:]))

class Solution:
    def addTwoNumbers(self, l1: t.Optional[ListNode], l2: t.Optional[ListNode]) -> t.Optional[ListNode]:
        answer = ListNode(0)
        cursor = answer
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total//10
            digit = total%10

            cursor.next = ListNode(digit)
            cursor = cursor.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return answer.next