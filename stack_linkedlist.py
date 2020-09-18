class Node:
  def __init__(self,val,next=None):
    self.val = val
    self.next = next


class Stack:
  def __init__(self,x):
     node = Node(x)
     self.head = node
     self.tail = node
  
  def push(self,x):
     node = Node(x)
     if self.head == None:
        self.head = node
     self.tail.next = node
     self.tail = node

  def pop(self):
     temp = self.head
     if temp.next == None:
       self.head = None
     while temp != None:
       if temp.next == self.tail:
         self.tail = temp
         temp.next = None
       temp = temp.next  
      
stacc = Stack(999)
stacc.push(88)
stacc.push(7)
temp = stacc.head
while temp != None:
  print(temp.val)
  temp = temp.next

stacc.pop()

stacc.pop()

stacc.pop()
stacc.push(78)
stacc.push(79)
temp = stacc.head
while temp != None:
  print(temp.val)
  temp = temp.next
     

  
     

    
    
    
    