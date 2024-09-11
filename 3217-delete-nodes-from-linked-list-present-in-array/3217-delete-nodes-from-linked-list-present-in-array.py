# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# review
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_to_remove = set(nums)

        while head and head.val in values_to_remove:
            head = head.next

        if not head:
            return None

        current = head
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next

        return head