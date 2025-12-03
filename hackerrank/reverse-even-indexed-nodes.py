def extractAndAppendSponsoredNodes(head):
    isEven = True
    cur = head
    
    evenHead = None
    oddHead = None
    oddTail = None
    
    while cur:
        nxt = cur.next 
        if isEven:
            cur.next = evenHead
            evenHead = cur
        else:
            if not oddHead:
                oddHead = cur
                oddTail = cur
            else:
                oddTail.next = cur
                oddTail = cur
            oddTail.next = None
        cur = nxt
        isEven = not isEven
    
    if not oddHead:
        return evenHead
    
    oddTail.next = evenHead
    return oddHead

# dummy head, tail을 종류별로 관리하는 아이디어