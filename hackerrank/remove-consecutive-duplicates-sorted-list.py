def deleteDuplicates(head):
    cur = head
    
    while cur:
        while cur.next and cur.next.data == cur.data:
            cur.next = cur.next.next
        cur = cur.next
            
    return head