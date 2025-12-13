# 21 merge two sorted lists

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


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    temp = dummy
    head1, head2 = list1, list2
    while head1 is not None and head2 is not None:
        if(head1.val <= head2.val):
            dummy.next = head1
            head1 = head1.next
        else:
            dummy.next = head2
            head2 = head2.next
        dummy = dummy.next
    if head1 is not None: # head1 remails
        dummy.next = head1
    if head2 is not None: # head2 remains
        dummy.next = head2
    return temp.next

list1 = [1,2,4,5,6,7,8]
list2 = [1,3,4]

head1 = create_linked_list(list1)
head2 = create_linked_list(list2)
display_linked_list(head1)
display_linked_list(head2)
display_linked_list(mergeTwoLists(head1,head2))