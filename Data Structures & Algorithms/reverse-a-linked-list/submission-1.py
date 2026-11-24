# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            next_val = head.next
            head.next = None
            while next_val:
                curr_val = next_val
                next_val = next_val.next
                curr_val.next = head
                head = curr_val
        return head
