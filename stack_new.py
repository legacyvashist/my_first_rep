class Node:
  def __init__(self,val,next=None):
    self.val = val
    self.next = next


class Stack:
  def __init__(self):
     self.head = None
     self.prev_tail = None
  
  def push(self,x):
     node = Node(x)
     if self.head is None:
         self.head = node
         self.prev_tail = None
         return None
     elif self.head.next is None:
         self.prev_tail=self.head
         self.head.next = node
         return None
     self.prev_tail.next.next = node
     self.prev_tail = self.prev_tail.next

  def pop(self):
      if self.head is None or self.prev_tail is None:
        pass
      elif self.head.next is None:
          self.head = self.prev_tail = None
      else:
     	  self.prev_tail.next = None 
      
stacc = Stack()
stacc.push(88)
stacc.push(7)
stacc.push(88)
stacc.push(7)

temp = stacc.head
while temp != None:
  print(temp.val)
  temp = temp.next

stacc.pop()

temp = stacc.head
while temp != None:
  print(temp.val)
  temp = temp.next

  
     

    
    
    
    