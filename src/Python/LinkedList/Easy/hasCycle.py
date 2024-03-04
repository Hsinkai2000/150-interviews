# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines whether a linked list has a cycle.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

s=Solution()
print(s.hasCycle([3,2,0,-4]))