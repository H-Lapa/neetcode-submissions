# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow and fast pointer to find the midpoint 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list 
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after

        list2 = prev

        # merge the two linkedlists     
        curr = head
        while list2:
            print(list2.val)
            after = curr.next
            curr.next = list2
            list2 = list2.next
            curr.next.next = after
            curr = after



        

