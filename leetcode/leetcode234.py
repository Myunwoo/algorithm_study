# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) 중간 찾기 (빠른 포인터는 2칸씩)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) 홀수 길이면 가운데 하나 건너뜀
        if fast:
            slow = slow.next

        # 3) 뒤 절반(slow부터)만 역순으로 뒤집기
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 4) 앞 절반(head)과 뒤집힌 뒤 절반(prev) 비교
        left, right = head, prev
        while right:               # 뒤 절반 길이만큼만 비교
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
