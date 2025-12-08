# loop 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        
        return prev


# 재귀 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        def reverse(head):
            nonlocal prev
            if not head:
                return prev
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            return reverse(head)
        
        return reverse(head)


