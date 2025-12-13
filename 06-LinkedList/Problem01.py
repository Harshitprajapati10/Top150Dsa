class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def display_linked_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

def reverseList(head):
    if(head is None or head.next is None):
        return head
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

arr = [1, 2, 3, 4, 5]
n = 2

head = create_linked_list(arr)
display_linked_list(head)
display_linked_list(removeNthFromEnd(head,n))