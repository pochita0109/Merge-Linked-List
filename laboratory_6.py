class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(list_1, list_2):
    dummy = ListNode(0)
    current = dummy

    while list_1 and list_2:
        if list_1.value <= list_2.value:
            current.next = list_1
            list_1 = list_1.next
        else:
            current.next = list_2
            list_2 = list_2.next
        current = current.next

    if list_1:
        current.next = list_1
    if list_2:
        current.next = list_2

    return dummy.next

list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)

merged_list = merge_two_lists(list_1, list_2)

print("Merged List:")
while merged_list:
    print(merged_list.value, end="->")
    merged_list = merged_list.next
print("None")