# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2 and list1:
            return
        
        result = None
        current = result
       
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                 if not result:
                     result = ListNode(pointer1.val)
                     current = result
                 else:
                     current.next = ListNode(pointer1.val)
                     current = ListNode(pointer1)
                 pointer1 = pointer1.next
            else:
                if not result:
                     result = ListNode(pointer2.val)
                     current = result
                else:
                     current.next = ListNode(pointer2.val)
                     current = ListNode(pointer2.val)
                pointer2 = pointer2.next

        if pointer2:
            while pointer2:
                if not result:
                     result = ListNode(pointer2.val)
                     current = result
                else:
                     current.next = ListNode(pointer2.val)
                     current = ListNode(pointer2.val)
                pointer2 = pointer2.next

        
        if pointer1:
            while pointer1:
                if not result:
                     result = ListNode(pointer1.val)
                     current = result
                else:
                     current.next = ListNode(pointer1.val)
                     current = ListNode(pointer2.val)
                pointer1 = pointer1.next
        return result