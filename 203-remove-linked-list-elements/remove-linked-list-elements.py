# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0,head)
        prev , curr = dummy , head
        while curr:
            next_node = curr.next
            if curr.val == val:
                prev.next = next_node
            else:
                prev = curr
            curr = next_node
        return dummy.next