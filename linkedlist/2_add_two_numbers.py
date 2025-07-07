# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newNode= ListNode()
        root=newNode
        c=0
        while l1 or l2 or c:
            n1=l1.val if l1 else 0
            n2=l2.val if l2 else 0
            num=n1+n2+c
            c=num//10
            num=num%10
            newNode.next=ListNode(num)
            newNode=newNode.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return root.next
            
        