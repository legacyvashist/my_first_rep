list = [1,2,3,4,5]
k = "m"
class Node:
 def __init__(self,nodeval):
   self.nodeval = nodeval
   self.next = None


for i in range(len(list)):
 obj_node = Node(list[i])
 if i == 0 :
   head = obj_node
   prev = head
   continue
 prev.next = obj_node 
 prev = prev.next

l = 0
temp = head
while temp != None:
  l = l + 1
  temp = temp.next
print("length",l)


temp = head
for i in range(1,l//2):
  temp = temp.next
obj_node = Node(k)
store = temp.next
temp.next = obj_node
obj_node.next = store

temp = head
while temp != None:
 print(temp.nodeval)
 temp = temp.next
 

  
 
   
 
 
  