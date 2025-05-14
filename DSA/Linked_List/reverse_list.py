class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        prev_node = None
        curr_node = head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        print(prev_node)
        while prev_node:
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next
        return True
    
class Solution1(object):
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
        
        