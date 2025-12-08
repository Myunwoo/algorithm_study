# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        head1 = l1
        head2 = l2
        carry = 0

        while head1 or head2 or carry:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            s = val1 + val2 + carry
            curVal = s % 10
            carry = s // 10

            cur.next = ListNode(curVal)
            cur = cur.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        return head.next
    
# 이 문제의 시간 복잡도는 l1의 길이를 n, l2의 길이를 m이라고 했을떄,
# O(max(n, m))으로 표현 가능

# l1과 l2의 참조를 헤치지 않는 선에서 head1, head2를 생성해서 문제를 풀었음
# 그러나, 추가 메모리를 쓰지 않는 방향으로 문제를 구현하라고 요청 받으면,
# l1,l2를 직접 사용하고, l1, l2중 한쪽을 결과 리스트로 사용하며,
# head에 더미 노드를 생성하지 않고 첫 노드의 존재 여부를 분기처리로 처리