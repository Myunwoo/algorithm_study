class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return head
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rightHead = None
        if fast.next:
            fast = fast.next
            rightHead = slow.next
        else:
            rightHead = slow
        
        # rightHead 부터 끝에 이르기까지 링크드리스트를 뒤집는다.
        prev = None
        while rightHead:
            cur = rightHead
            rightHead = cur.next
            cur.next = prev
            prev = cur

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True