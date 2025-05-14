class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        pre_head = ListNode(-1)
        prev = pre_head
        while head:
            if head.val not in prev:
                prev.next = head
                head = head.next
            else:
                head = head.next
            
        return pre_head.next