# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 'prev' will point to the previous node.
        # Initially, there is no previous node.
        prev = None

        # 'temp' is used to traverse the linked list.
        temp = head

        # Traverse until we reach the end of the list.
        while temp:

            # Store the next node before changing the link.
            next_val = temp.next

            # Reverse the current node's pointer.
            temp.next = prev

            # Move 'prev' one step forward.
            prev = temp

            # Move 'temp' to the next node.
            temp = next_val

        # 'prev' becomes the new head of the reversed list.
        return prev