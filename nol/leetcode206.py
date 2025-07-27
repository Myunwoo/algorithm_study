# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        cur = head
        next = cur.next

        while cur:
            cur.next = prev
            prev = cur
            if not next:
                break
            cur = next
            next = cur.next
        
        return cur
        