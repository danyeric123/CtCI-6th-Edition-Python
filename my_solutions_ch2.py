


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
      return f'Node value: {self.val} Node next: {self.next}'


def kth_to_last(head,k):
  runner = current = head
  
  for _ in range(k):
    if not runner:
      return None
    runner = runner.next 
    
  while runner:
    current = current.next
    runner = runner.next
    
  return current

# This is the same as doing one round of quick sort but with linkedlist
# So you would have two lists, one for less and one for greater and add to each
def partition(head):
  h1 = l1 = ListNode(0)
  h2 = l2 = ListNode(0)
  while head:
      if head.val < x:
          l1.next = head
          l1 = l1.next
      else:
          l2.next = head
          l2 = l2.next
      head = head.next
  l2.next = None
  l1.next = h2.next
  return h1.next

def addTwoNumbers(l1,l2):
        num1, num2 = l1, l2
        carry = 0
        cur = new_list = ListNode()
        
        while num1 or num2:
            result = carry
            
            if num1:
                result += num1.val
                num1 = num1.next
            if num2:
                result += num2.val
                num2 = num2.next
            
            cur.next = ListNode(val=result%10)
            cur = cur.next
            
            carry = result // 10
            
        if carry:
            cur.next = ListNode(val=carry)
            
        return new_list.next
      
def palindrome(head):
  fast = slow = head
  stack = []
  
  while fast and fast.next:
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next 
  
  if fast:
    slow = slow.next 
    
  while slow:
    top = stack.pop()
    
    if top != slow.val:
      return False
    
    slow = slow.next
    
  return True

# node4 = ListNode(val=1)
# node3 = ListNode(val=2,next=node4)
# node2 = ListNode(val=2,next=node3)
# node1 = ListNode(val=1,next=node2)

# print(palindrome(node1))

def get_intersection(headA, headB):
  currA, currB = headA, headB
  
  while currA != currB:
      currB = headA if currB is None else currB.next
      currA = headB if currA is None else currA.next
      
  return currA

def loop_detection(head):
  visited = set()
  cur = head
  
  while cur:
    if cur in visited:
      return cur
    visited.add(cur)
    cur = cur.next

# node5 = ListNode(val="e")
# node4 = ListNode(val="d",next=node5)
# node3 = ListNode(val="c",next=node4)
# node5.next = node3
# node2 = ListNode(val="b",next=node3)
# node1 = ListNode(val="a",next=node2)

# print(loop_detection(node1))