class Node:
 def __init__(self,data,next = None):
   self.data = data
   self.next = next
 
class Stack:
  def __init__(self):
   self.head = None
  
  def isempty(self):
     if self.head == None:
       return True  
     else:
       return False
  def push(self,data):
     if self.head == None:
       newnode = Node(data)
       self.head = newnode
     else:
       newnode = Node(data)
       newnode.next = self.head
       self.head = newnode
  
  def pop(self):
     if isempty():
       return None
     else:
       temp = self.head
       temp2 = self.head.next
       self.head.next = None
       self.head = temp2
       return temp
stack1 = Stack()
stack1.push(99)
stack1.push(88)
stack1.push(77)
temp = stack1.head
while temp:
  print(temp.data)
  temp = temp.next