# Problem: Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Approach: Traverse the linked list and skip duplicate nodes
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head  # Start from head of linked list
        
        # Traverse until end of list
        while curr and curr.next:
            
            # If current node and next node have same value
            if curr.val == curr.next.val:
                
                # Skip the duplicate node
                curr.next = curr.next.next
            
            else:
                # Move to next node
                curr = curr.next
        
        return head