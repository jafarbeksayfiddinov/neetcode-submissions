# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index=0
        hashset=set()
        while head is not None:
            if head in hashset:
                return True
            hashset.add(head)
            head=head.next
            index+=1
        
        return False