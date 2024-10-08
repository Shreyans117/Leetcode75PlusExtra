#1. O(1) Space Complexity Solution.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead=None
        if not head:
            return head
        def dfs(node):
            nonlocal newHead
            if node.next:
                curr=dfs(node.next)
                curr.next=node
                return node
            else:
                newHead = node
                return node
        tail=dfs(head)
        tail.next=None
        return newHead
#2. O(n) Space Complexity Solution.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        stack=[]
        iter=head
        while iter!=None:
            stack.append(iter)
            iter=iter.next
        head=stack.pop()
        iter=head
        while len(stack)!=0:
            iter.next=stack.pop()
            iter=iter.next
        iter.next=None
        return head

