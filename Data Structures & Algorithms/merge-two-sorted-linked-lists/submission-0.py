# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNode=None
        tailNode=None
        while (list1 and list2) is not None:
            temp1=list1.next
            temp2=list2.next
            if list1.val<list2.val:
                if headNode is None:
                    headNode=list1
                    tailNode=list1
                else:
                    tailNode.next=list1
                    tailNode=tailNode.next
                list1=temp1
            elif list1.val>list2.val:
                if headNode is None:
                    headNode=list2
                    tailNode=list2
                else:
                    tailNode.next=list2
                    tailNode=tailNode.next
                list2=temp2
            else:
                if headNode is None:
                    headNode=list1
                    tailNode=list1
                else:
                    tailNode.next=list1
                    tailNode=tailNode.next
                tailNode.next=list2
                tailNode=tailNode.next
                list1=temp1
                list2=temp2
        if list1 is not None:
            if headNode is None:
                headNode=list1
            else:
                tailNode.next=list1
                tailNode=list1
        if list2 is not None:
            if headNode is None:
                headNode=list2
            else:
                tailNode.next=list2
                tailNode=list2
        return headNode
            
            

