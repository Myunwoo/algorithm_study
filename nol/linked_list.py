class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group_order(head: ListNode, k: int) -> ListNode:
    if not head or k <= 1:
        return head

    # 길이 계산
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    r = n % k  # 첫 블록 크기(나머지), 0이면 첫 블록도 k

    # 전체 뒤집기
    head = reverse_segment(head, n)  # n개 전부 뒤집기

    # 블록 단위 재뒤집기: 첫 블록은 r(0이면 k), 이후는 k씩
    dummy = ListNode(0, head)
    prev = dummy
    cur = head

    first_block = r if r != 0 else k
    sizes = [first_block] + [k] * ((n - first_block) // k)

    for size in sizes:
        # size개의 구간을 뒤집는다
        new_head, new_tail, next_start = reverse_first_m(cur, size)
        # prev -> (뒤집힌구간 head)
        prev.next = new_head
        # tail -> 다음 시작
        new_tail.next = next_start
        # 포인터 전진
        prev = new_tail
        cur = next_start

    return dummy.next

def reverse_segment(head: ListNode, m: int) -> ListNode:
    """앞에서 m개를 통째로 뒤집어 새로운 head 반환"""
    prev, cur = None, head
    for _ in range(m):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev  # 새 head

def reverse_first_m(head: ListNode, m: int):
    """head부터 m개 노드를 뒤집고 (new_head, new_tail, next_start) 반환"""
    prev, cur = None, head
    for _ in range(m):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # prev: 뒤집힌 구간의 head, head: 뒤집힌 구간의 tail, cur: 다음 시작
    return prev, head, cur
