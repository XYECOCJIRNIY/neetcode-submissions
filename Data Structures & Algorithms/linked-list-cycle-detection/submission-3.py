# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and slow:
            fast = fast.next
            slow = slow.next
            if fast and slow:
                fast = fast.next
                if fast and slow:
                    if slow.val == fast.val:
                        return True
            else:
                return False

        return False
        