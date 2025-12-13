#143 reorder list


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
    if head is None or head.next is None:
        return head
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

def getMid(head):
    f,s = head, head
    while(f is not None and f.next is not None):
        s = s.next
        f = f.next.next
    return s

def reOrderList(head):
    if(head is None or head.next is None):
        return
    mid = getMid(head)
    second = reverseList(mid.next)
    mid.next = None
    first = head # 1,2,3
    # rearrange
    while second:
        t1 = first.next
        t2 = second.next        
        first.next = second
        second.next = t1
        first = t1
        second = t2
    return head

head = [1,2,3,4,5,6,7]
head1 = create_linked_list(head)
display_linked_list(head1)
# display_linked_list(reverseList(head1))
# print(getMid(head1).val) #4

display_linked_list(reOrderList(head1))