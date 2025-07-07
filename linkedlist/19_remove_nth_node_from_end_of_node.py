# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        k = 0
        curr = head
        while curr:
            curr = curr.next
            k+=1
        if k == 1:
            return None
        if k == n:
            return head.next
        node = k - n - 1
        curr = head
        for _ in range(node):
            curr = curr.next
        curr.next = curr.next.next
        return head