# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        needAdd = False
        head = ListNode()
        cur = head

        while True:
            if not l1 and not l2:
                break
            curNode = ListNode()

            if l1 and l2:
                curNode.val = l1.val + l2.val + (1 if needAdd else 0)
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                curNode.val = l1.val + (1 if needAdd else 0)
                l1 = l1.next
            elif not l1 and l2:
                curNode.val = l2.val + (1 if needAdd else 0)
                l2 = l2.next
            
            if curNode.val >= 10:
                curNode.val %= 10
                needAdd = True
            else:
                needAdd = False
            
            cur.next = curNode
            cur = cur.next
        
        if needAdd:
            curNode = ListNode()
            curNode.val = 1
            cur.next = curNode
        
        return head.next