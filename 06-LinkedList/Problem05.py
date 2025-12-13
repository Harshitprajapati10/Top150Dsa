# 19 remove nth from the end of the list

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
