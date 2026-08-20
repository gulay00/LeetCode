# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
