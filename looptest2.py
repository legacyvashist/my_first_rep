list = [1,2,3,4,5,6,7,8,9,10]
class Node :
 def __init__(self,value):
  self.value = value
  self.next = None
#listcreation
for i in range(len(list)):
  obj = Node(list[i])
  if i == 0:
   head = obj
   prev = head
   continue
  prev.next = obj
  prev = prev.next
k = 'm'
jumper = head
jumper2 = head
temp = head
while jumper != None and jumper.next != None:
 jumper = jumper.next.next
 jumper2 = jumper2.next
print(jumper2.value)
obj = Node(k)
store = jumper2.next
jumper2.next = obj
obj.next = store

while temp != None:
 print(temp.value)
 temp = temp.next


 

 
