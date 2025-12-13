# add two numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def createNode(val):
    return ListNode(val)
def addTwoNumbers(l1, l2):
    f, s = l1, l2
    dummy = createNode(0)
    cur = dummy
    carry = 0

    while f is not None or s is not None or carry != 0:
        total = carry

        if f is not None:
            total += f.val
            f = f.next

        if s is not None:
            total += s.val
            s = s.next

        cur.next = createNode(total % 10)
        cur = cur.next
        carry = total // 10

    return dummy.next
# Helper to create list from array
def create_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# Input
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])

# Output
res = addTwoNumbers(l1, l2)

# Print result
while res:
    print(res.val, end=" -> ")
    res = res.next
print("None")
