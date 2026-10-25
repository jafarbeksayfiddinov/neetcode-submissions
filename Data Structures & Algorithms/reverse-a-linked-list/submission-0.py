# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headNode=None
        while head is not None:
            temp=head.next
            head.next=headNode
            headNode=head
            head=temp
        return headNode