"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp_head=head
        copy_node=None
        beginning=None
        dic={}
        while temp_head:
            s=Node(temp_head.val,None,None)

            if copy_node is None:
                copy_node=s
                beginning=copy_node
            else:
                copy_node.next=s
                copy_node=copy_node.next
            
            dic[temp_head]=copy_node
            temp_head=temp_head.next
        while head:
            copy_ref=dic[head]
            if head.random:
                copy_ref.random=dic[head.random]
            head=head.next
        
        return beginning

