# 링크드 리스트 노드 정의 예시 (Hackerrank 환경에 이미 있을 수도 있음)
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeKthFromEnd(head: SinglyLinkedListNode, k: int) -> SinglyLinkedListNode:
    # 빈 리스트면 그대로 반환
    if head is None:
        return head

    # k가 "끝에서 0-based" → 1-based로는 n = k + 1 번째 from end
    n = k + 1

    # 더미 노드: head 삭제 케이스도 한 번에 처리하기 위해 사용
    dummy = SinglyLinkedListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # fast를 먼저 n칸 앞으로 보낸다
    # 만약 그 전에 fast.next가 None이면, n > 길이 → k가 invalid → 원본 그대로 반환
    for _ in range(n):
        if fast.next is None:
            # 리스트 길이 < n 이므로 k가 invalid
            return head
        fast = fast.next

    # 이제 fast가 끝에 도달할 때까지 fast/slow 같이 한 칸씩 이동
    # fast가 마지막 노드를 가리킬 때 slow는 "삭제 대상의 이전 노드"를 가리키게 됨
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # slow.next 가 실제로 삭제할 노드
    slow.next = slow.next.next

    # 새 head 반환 (head가 삭제된 경우 dummy.next가 새로운 head)
    return dummy.next

# fast가 먼저가고, slow가 뒤따라 가는 방식으로 풀이하는 문제가 이런 유형도 있다.
# fast만 먼저 몇 칸 보내놓고, 끝에 다다를 때까지 fast와 slow를 이동시키면, slow가 어디에 위치하게 되는가?
# 이런 아이디어가 필요한 문제.