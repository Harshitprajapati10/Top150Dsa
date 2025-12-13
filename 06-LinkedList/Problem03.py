# linked list cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(self, head):
    s, f = head, head
    while f is not None and f.next is not None:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False
