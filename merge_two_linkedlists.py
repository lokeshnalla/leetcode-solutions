# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node to simplify the merging process
        dummy = ListNode()

        # Pointer used to build the merged list
        temp = dummy

        # Compare nodes until one list becomes empty
        while list1 and list2:

            # If list1's value is smaller, attach it
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next

            # Otherwise attach list2's node
            else:
                temp.next = list2
                list2 = list2.next

            # Move temp forward
            temp = temp.next

        # Attach remaining nodes (if any)
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        # Return merged list (skip dummy node)
        return dummy.next