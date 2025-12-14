# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = ListNode()
        prev.next = head

        cur = head
        if cur.next:
            head = cur.next
        
        while cur:
            nxt = cur.next
            if not nxt:
                break
            
            temp = nxt.next
            cur.next = temp
            nxt.next = cur
            prev.next = nxt
            prev = cur
            cur = temp
        
        return head