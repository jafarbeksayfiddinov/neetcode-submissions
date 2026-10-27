# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mid=None
        slow=head
        fast=head
        b=head
        while (fast and fast.next) is not None:
            fast=fast.next.next
            slow=slow.next
        if slow==fast:
            return
        mid=slow
        reverse=None
        while slow is not None:
            temp=slow
            slow=slow.next
            temp.next=reverse
            reverse=temp
        head=None
        while b!=mid:
            temp1=b.next
            temp2=reverse.next
            b.next=None
            reverse.next=None
            if head is None:
                head=b
                head.next=reverse
                head=head.next
            else:
                head.next=b
                head.next.next=reverse
                head=head.next.next
            b=temp1
            reverse=temp2
        if reverse:
            head.next=reverse

        