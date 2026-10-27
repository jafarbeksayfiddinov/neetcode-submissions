# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        clone=head
        size=0
        while clone:
            size+=1
            clone=clone.next
        clone=head
        if size==1 and n==1:
            return None
        index=0
        r=size-n-1
        if r<0:
            head=head.next
        else:
            while clone:
                if index==r:
                    clone.next=clone.next.next
                clone=clone.next
                index+=1
        return head
