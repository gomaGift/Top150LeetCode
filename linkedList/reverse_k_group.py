from typing_extensions import Optional


class ListNode:
    def __init__(self, val : int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         tail = head
         for i in range(k):
            if not tail:
                 return head
            tail = tail.next

         def reverse(curr, end):
             prev = None

             while curr != end:
                 temp = curr.next
                 curr.next = prev
                 prev = curr
                 curr = temp
             return prev

         new_head = reverse(head, tail)
         head.next = self.reverse_k_group(tail, k)
         return new_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

test = Solution()
print(test.reverse_k_group(node1, 2).val)
